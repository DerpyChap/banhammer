from banhammer import Generator

# Setup the generator
g = Generator()

# Generate the GIF (returns a BytesIO object)
im = g.image_gen('Example')

# Write the image to a file called output.gif
f = open('output.gif', 'wb')
f.write(im.read())
f.close()
