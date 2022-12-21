from PIL import Image, ImageFont, ImageDraw
import io
import os
import numpy
import imageio
import json


class Generator:
    """HAMMER DOWN!"""

    def __init__(self):
        self.size_check = 10
        self.target_size = (1200, 225)
        self.basedir = os.path.dirname(os.path.abspath(__file__))
        self.frames = sorted(os.listdir(f'{self.basedir}/frames/'))
        with open(f'{self.basedir}/frames.json') as f:
            j = json.load(f)
            self.metadata = {}
            for key, coords in j.items():
                cset = []
                for c in coords:
                    cset.append(tuple(c))
                self.metadata[key] = cset

    # From https://stackoverflow.com/a/53092540
    def find_coeffs(self, source_coords, target_coords):
        matrix = []
        for s, t in zip(source_coords, target_coords):
            matrix.append([t[0], t[1], 1, 0, 0, 0, -s[0] * t[0], -s[0] * t[1]])
            matrix.append([0, 0, 0, t[0], t[1], 1, -s[1] * t[0], -s[1] * t[1]])
        A = numpy.matrix(matrix, dtype=numpy.float64)
        B = numpy.array(source_coords).reshape(8)
        res = numpy.dot(numpy.linalg.inv(A.T * A) * A.T, B)
        return numpy.array(res).reshape(8)

    def get_anchor_points(self, size: tuple):
        x_middle = size[0] / 2
        x_left = x_middle - 600
        x_right = x_middle + 600
        coords = [(x_left, 0), (x_right, 0), (x_right, size[1]),
                  (x_left, size[1])]
        return coords

    def multiply_coords(self, coords):
        """Used for antialiasing text."""
        new = []
        for t in coords:
            new.append(tuple(i * 2 for i in t))
        return new

    def draw_outline(self, draw_obj, text, x, y, font):
        """Adds an outline to the text."""
        draw_obj.text((x - 3, y - 3), text, (159, 115, 110, 255), font=font)
        draw_obj.text((x + 3, y - 3), text, (159, 115, 110, 255), font=font)
        draw_obj.text((x + 3, y + 3), text, (159, 115, 110, 255), font=font)
        draw_obj.text((x - 3, y + 3), text, (159, 115, 110, 255), font=font)
        draw_obj.text((x, y), text, (255, 153, 126, 255), font=font)
        return

    def image_gen(self, text: str):
        """Generates the GIF."""
        text = text.upper()
        font = ImageFont.truetype(font=f'{self.basedir}/assets/Bungee-Regular.ttf', size=200)

        font_size = font.getsize(text)

        text_img = Image.new('RGBA', font_size, (0, 0, 0, 0))

        d = ImageDraw.Draw(text_img)
        self.draw_outline(d, text, 3, 3, font)

        final_text = text_img.crop(text_img.getbbox())
        points = self.get_anchor_points(final_text.size)

        frame = 0
        output = io.BytesIO()
        with imageio.get_writer(
                output, mode='I', format='GIF', duration=0.04) as writer:
            for filename in self.frames:
                path = f'{self.basedir}/frames/{filename}'
                coords = self.metadata.get(str(frame + 1), {})
                if coords:
                    f = Image.open(path).convert('RGBA')
                    coeffs = self.find_coeffs(points,
                                              self.multiply_coords(coords))
                    new_im = final_text
                    new_im = new_im.transform(
                        tuple(i * 2 for i in f.size), Image.PERSPECTIVE, coeffs,
                        Image.BILINEAR)
                    new_im = new_im.resize(f.size, Image.ANTIALIAS)
                    f.paste(new_im, mask=new_im)
                    imgbytes = io.BytesIO()
                    f.save(imgbytes, format='GIF')
                    imgbytes.seek(0)
                    image = imageio.imread(imgbytes, format='gif')
                    writer.append_data(image)
                else:
                    image = imageio.imread(path)
                    writer.append_data(image)
                frame += 1

        output.seek(0)
        return output
