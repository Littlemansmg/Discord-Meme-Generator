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
import discord
from datetime import datetime as dt
# import logging

toplist = ['mocking-spongebob']
bottomlist = []

topBottomList = [
    '10-guy', 'bad-luck-brian', 'good-guy-greg', 'roll-safe',
    'simply', 'successkid', 'willy-wonka']

with open('token.txt') as token:
    token = token.readline()

listhelp = 'Prints a list of all the memes available.'

tbhelp = 'Prints top and bottom text memes.\n' \
         'Notes: This command can only be used with memes that are in the Top and Bottom List. ' \
         '\nTEXT MUST BE IN SINGLE OR DOUBLE QUOTES.'

tophelp = 'Prints top text memes.\n' \
          'Notes: This command will only print toptext. It can only be used with memes that are in the Top List ' \
          'or Top and Bottom list. \nTEXT MUST BE IN SINGLE OR DOUBLE QUOTES.'

bottomhelp = 'Prints bottom text memes.\n' \
             'Notes: This command will only print bottomtext. It can only be used with memes that are in the ' \
             'Bottom List or Top and Bottom list. \nTEXT MUST BE IN SINGLE OR DOUBLE QUOTES.'

# logger = logging.getLogger('discord')
# logger.setLevel(logging.DEBUG)
# handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
# handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
# logger.addHandler(handler)

bot = commands.Bot(command_prefix=')')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('----------')
    await bot.change_presence(game = discord.Game(name = "Type )help for help"))

@bot.event
async def on_command_error(error, ctx):
    # NOTE: It's stated in the documentation that CTX, should always be first.
    # for on_command_error, The first paramater is the error, and then the context
    # so error will always come first.
    destination = ctx.message.channel
    if isinstance(error, commands.MissingRequiredArgument):

        with open('command_log.txt', 'a') as log:
            now = dt.now().strftime('%m-%d_%H:%M:%S')
            log.write(now + ' ERROR: MissingRequiredArgument ' + str(ctx.message.author) + ' ' +
                      str(ctx.message.content) + '\n')

        await bot.delete_message(ctx.message)
        await bot.send_message(destination, "You are missing some arguments.")

@bot.command(pass_context=True, name='tb', description = "Prints top and bottom text.", help = tbhelp)
async def topAndBottom(ctx, memeType, topString : str, bottomString : str):
    destination = ctx.message.channel
    message = ctx.message

    await bot.delete_message(message)

    if memeType in topBottomList:
        send = top_bottom(memeType, topString, bottomString)
        await bot.send_file(destination, send)
        with open('command_log.txt', 'a') as log:
            now = dt.now().strftime('%m-%d_%H:%M:%S')
            log.write(now + ' INFO: Command Used ' + str(ctx.message.author) + ' ' +
                      str(ctx.message.content) + "\n")

    else:
        await bot.send_message(destination, "Sorry, " + memeType + " isn't available or not in this list.")
        with open('command_log.txt', 'a') as log:
            now = dt.now().strftime('%m-%d_%H:%M:%S')
            log.write(now + ' WARNING: Meme Missing ' + str(ctx.message.author) + ' ' +
                      str(ctx.message.content) + "\n")

@bot.command(pass_context = True, name = 'top',description = "Prints top atext.", help = tophelp)
async def topText(ctx, memeType, topString):
    destination = ctx.message.channel
    message = ctx.message

    await bot.delete_message(message)

    if memeType in toplist:
        send = top_bottom(memeType, topString, '')
        await bot.send_file(destination, send)
        with open('command_log.txt', 'a') as log:
            now = dt.now().strftime('%m-%d_%H:%M:%S')
            log.write(now + ' INFO: Command Used ' + str(ctx.message.author) + ' ' +
                      str(ctx.message.content) + "\n")

    elif memeType in topBottomList:
        send = top_bottom(memeType, topString, '')
        await bot.send_file(destination, send)
        with open('command_log.txt', 'a') as log:
            now = dt.now().strftime('%m-%d_%H:%M:%S')
            log.write(now + ' INFO: Command Used ' + str(ctx.message.author) + ' ' +
                      str(ctx.message.content) + "\n")

    else:
        await bot.send_message(destination, "Sorry, " + memeType + " isn't available or not in this list.")
        with open('command_log.txt', 'a') as log:
            now = dt.now().strftime('%m-%d_%H:%M:%S')
            log.write(now + ' WARNING: Meme Missing ' + str(ctx.message.author) + ' ' +
                      str(ctx.message.content) + "\n")

@bot.command(pass_context = True, name = 'bottom',description = "Prints bottom text.", help = bottomhelp)
async def bottomText(ctx, memeType, bottomString):
    destination = ctx.message.channel
    message = ctx.message

    await bot.delete_message(message)

    if memeType in toplist:
        send = top_bottom(memeType, '', bottomString)
        await bot.send_file(destination, send)
        with open('command_log.txt', 'a') as log:
            now = dt.now().strftime('%m-%d_%H:%M:%S')
            log.write(now + ' INFO: Command Used ' + str(ctx.message.author) + ' ' +
                      str(ctx.message.content) + "\n")

    elif memeType in topBottomList:
        send = top_bottom(memeType, '', bottomString)
        await bot.send_file(destination, send)
        with open('command_log.txt', 'a') as log:
            now = dt.now().strftime('%m-%d_%H:%M:%S')
            log.write(now + ' INFO: Command Used ' + str(ctx.message.author) + ' ' +
                      str(ctx.message.content) + "\n")

    else:
        await bot.send_message(destination, "Sorry, " + memeType + " isn't available or not in this list.")
        with open('command_log.txt', 'a') as log:
            now = dt.now().strftime('%m-%d_%H:%M:%S')
            log.write(now + ' ' + str(ctx.message.author) + ' ' +
                      str(ctx.message.content) + " WARNING: Meme Missing.\n")

@bot.command(pass_context = True, name = 'list', description = "Prints a list of memes.", help = listhelp)
async def listMemes(ctx):
    destination = ctx.message.channel
    message = ctx.message

    await bot.delete_message(message)

    tmptop = ", ".join(toplist)
    tmpbottom = ", ".join(bottomlist)
    tmptb = ", ".join(topBottomList)

    await bot.send_message(destination, 'Top text only: ' + tmptop)
    await bot.send_message(destination, 'Bottom text only: ' + tmpbottom)
    await bot.send_message(destination, 'Top and Bottom text: ' + tmptb)
    with open('command_log.txt', 'a') as log:
        now = dt.now().strftime('%m-%d_%H:%M:%S')
        log.write(now + ' INFO: Command Used ' + str(ctx.message.author) + ' ' +
                  str(ctx.message.content) + "\n")

bot.run(token.strip())
