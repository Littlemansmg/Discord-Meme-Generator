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

import PIL.Image as Image
import PIL.ImageFont as IFont
import PIL.ImageDraw as IDraw

def make_meme(memetype):
    with Image.open(memetype + ".jpg") as img:
        font = IFont.truetype("impact.ttf", 30)
        edit = IDraw.Draw(img)

        edit.text((10,10),"When pillow Works", font=font)
        img.save(memetype + '_new.jpg')

if __name__ == '__main__':

    meme = 'successkid'

    make_meme(meme)
