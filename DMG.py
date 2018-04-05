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

toplist = ['simply']

topBottomList = [
    '10-guy', 'bad-luck-brian', 'good-guy-greg', 'mocking-spongebob', 'roll-safe',
    'successkid', 'willy-wonka']

with open('token.txt') as token:
    token = token.readline()


bot = commands.Bot(command_prefix=')')
@bot.event
async def on_ready():

    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('----------')
    # bot.change_presence(game = ")help for help")

@bot.event()
async def on_error(event, *args, **kwargs):
    await bot.say("YOU FUCKED UP")

@bot.command(pass_context=True, name='tb')
async def topAndBottom(ctx, memeType, topString, bottomString):
    if commands.MissingRequiredArgument:
        await bot.say("Sorry, you need to fill in all 3 paramaters with text or (\"\"). Ex. `)tb bad-luck-brian "
                      "\"Reads help for commands\" "
                      "\"Still can't type them in right\"")

    destination = ctx.message.channel
    message = ctx.message
    await bot.delete_message(message)

    if memeType in toplist:
        send = top_bottom(memeType, topString, '')
        await bot.send_file(destination, send)

    elif memeType in topBottomList:
        send = top_bottom(memeType, topString, bottomString)
        await bot.send_file(destination, send)

    else:
        await bot.send_message(destination, "Sorry @" + str(ctx.message.author) + ", " + memeType + " isn't here.")

bot.run(token)
