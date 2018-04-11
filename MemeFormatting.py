# https://github.com/danieldiekmeier/memegenerator

import PIL.Image as Image
import PIL.ImageFont as IFont
import PIL.ImageDraw as IDraw
import os
import random as rand


def top_bottom(memetype, topString, bottomString):
    if memetype == "mocking-spongebob":
        bottomString = ''
        for i in range(len(topString)):
            if rand.randint(0,1) == 0:
                bottomString += topString[i].upper()
            else:
                bottomString += topString[i].lower()

    try:
        with Image.open(os.path.relpath('Templates/' + memetype + '.jpg')) as img:
            size = img.size
            fontSize = int(size[1] / 5)
            font = IFont.truetype("impact.ttf", fontSize)

            edit = IDraw.Draw(img)

            # find biggest font size that works

            topTextSize = font.getsize(topString)
            bottomTextSize = font.getsize(bottomString)
            while topTextSize[0] > size[0] - 20 or bottomTextSize[0] > size[0] - 20:
                fontSize = fontSize - 1
                font = IFont.truetype("impact.ttf", fontSize)
                topTextSize = font.getsize(topString)
                bottomTextSize = font.getsize(bottomString)

            # find top centered position for top text
            topTextPositionX = (size[0] / 2) - (topTextSize[0] / 2)
            topTextPositionY = 0
            topTextPosition = (topTextPositionX, topTextPositionY)

            # find bottom centered position for bottom text
            bottomTextPositionX = (size[0] / 2) - (bottomTextSize[0] / 2)
            bottomTextPositionY = size[1] - bottomTextSize[1] - 10
            bottomTextPosition = (bottomTextPositionX, bottomTextPositionY)

            # draw outlines
            # there may be a better way
            outlineRange = int(fontSize / 15)
            for x in range(-outlineRange, outlineRange + 1):
                for y in range(-outlineRange, outlineRange + 1):
                    edit.text((topTextPosition[0] + x, topTextPosition[1] + y), topString, (0, 0, 0), font=font)
                    edit.text((bottomTextPosition[0] + x, bottomTextPosition[1] + y), bottomString, (0, 0, 0), font=font)

            edit.text(topTextPosition, topString, (255, 255, 255), font=font)
            edit.text(bottomTextPosition, bottomString, (255, 255, 255), font=font)
            img.save(os.path.relpath('New/' + memetype + '_new.jpg'))
    except FileNotFoundError:
        print('Sorry, that template doesn\'t exist.')
    return os.path.relpath('New/' + memetype + '_new.jpg')
