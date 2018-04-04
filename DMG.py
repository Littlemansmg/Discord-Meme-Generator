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

from MemeFormatting import *
from discord.ext import commands

topBottomList = [
    '10-guy', 'bad-luck-brian', 'good-guy-greg', 'mocking-spongebob', 'roll-safe',
    'simply', 'successkid', 'willy-wonka']

if __name__ == '__main__':

    meme = input("What's the Meme type? ")
    if meme in topBottomList:
        topText = input('Top Text: ')
        bottomText = input('Bottom Text: ')

        top_bottom(memetype=meme, topString=topText, bottomString=bottomText)
    else:
        print('Sorry can\'t do that.')

# ---------------- Discord code ----------------

bot = commands.Bot(command_prefix=')')
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('----------')

@bot.command(name='tb')
async def topAndBottom(ctx, memeType : str, topString : str, bottomString : str):
    ctx.message.delete()
    if memeType in topBottomList:
        await ctx.send(file=top_bottom(memeType, topString, bottomString))
    else:
        await ctx.send('Sorry, not a memetype.')

bot.run('token')