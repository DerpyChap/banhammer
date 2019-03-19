# Tom Scott Banhammer Generator
_Generates GIFs based on Tom Scott's Banhammer_

![](https://i.imgur.com/l1CdgDm.gif)

Want to use this in any project using Docker? Get the Docker container here: https://gitlab.com/nerd3-servers/banhammer-generator

## Installing
**Python 3.5+ is required**

To install the library, simply run the following command:

```
pip install banhammer
```

If you would like to use a `pillow` drop-in replacement, such as `pillow-simd`, then install that prior to installing the banhammer. All requirements should automatically install.

## Usage
`banhammer.Generator()` is the main generator object. To generate an image, use `Generator().image_gen(str)` where `str` is your string of choice. This will return an `io.BytesIO()` object, which you can then manually write to a file or upload somewhere.

### Example
The following example generates a GIF and saves it to a file called `output.gif`:

```python
from banhammer import Generator

# Setup the generator
g = Generator()

# Generate the GIF (returns a BytesIO object)
im = g.image_gen('Example')

# Write the image to a file called output.gif
f = open('output.gif', 'wb')
f.write(im.read())
f.close()
```

The resulting GIF looks something like this:

![](https://i.imgur.com/TUOye1z.gif)

## Font Licensing
The font file included is a modified version of the Bungee Regular font. The font has been modified to include missing unicode characters and emoji provided by other fonts. The licensing and source information can be found below.

| Font | Designers | Licenses |
| ---- | ---------------- | ------- |
|[Bungee Regular](https://fonts.google.com/specimen/Bungee)|[David Jonathan Ross](http://www.djr.com/)|[SIL Open Font License](https://github.com/DerpyChap/banhammer/blob/master/banhammer/assets/Bungee-LICENSE.txt)
|[Twitter Color Emoji SVGinOT Font](https://github.com/twitter/twemoji)|[Brad Erickson](https://keybase.io/bde), [Joe Loughry](https://cnadocs.com/), Terence Eden, [Twitter, Inc](https://about.twitter.com/en_us/company.html) and collaborators|[Massachusetts Institute of Technology License](https://github.com/DerpyChap/banhammer/blob/master/banhammer/assets/twitter-color-emoji-LICENSE.txt)<br/>[Creative Commons Attribution 4.0 International](https://github.com/DerpyChap/banhammer/blob/master/banhammer/assets/twitter-color-emoji-LICENSE.txt#L24)
|[DejaVu Sans Mono](https://dejavu-fonts.github.io/)|[Štěpán Roh](http://alivebutsleepy.srnet.cz/) and [authors](https://dejavu-fonts.github.io/Authors.html), [Bitstream, Inc](https://www.monotype.com/), [Tavmjung Bah](https://tavmjong.free.fr/)|[Massachusetts Institute of Technology License](https://github.com/DerpyChap/banhammer/blob/master/banhammer/assets/DejaVu-LICENSE.txt)
|[Tetsubin Gothic](http://fontna.com/freefont/?p=12)|[フォントな自由](http://fontna.com/)|[Apache License 2.0](https://github.com/DerpyChap/banhammer/blob/master/banhammer/assets/Tetsubin-LICENSE.txt)
