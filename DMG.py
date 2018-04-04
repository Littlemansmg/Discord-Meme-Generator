"""
Discord-Meme-Generator by Scottie (LittlemanSMG) Goes
4/4/2018
This program is built to allow discord users to type a command and then
fill in top/bottom text. This image will be created and then posted
in the channel that the message came from.

Pillow:
    https://pillow.readthedocs.io/en/5.1.x/

Github: https://github.com/Littlemansmg/Discord-Meme-Generator
"""

import PIL.ImageFilter as IFilter
import PIL.Image as Image

def make_meme(memetype):
    with Image.open(memetype + ".jpg") as img:
        img.save(memetype + '_new.jpg')

if __name__ == '__main__':

    meme = 'successkid'

    make_meme(meme)
