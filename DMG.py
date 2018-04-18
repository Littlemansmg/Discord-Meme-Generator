"""
Discord-Meme-Generator by Scottie (LittlemanSMG) Goes
4/4/2018
This program is built to allow discord users to type a command and then
fill in top/bottom text. This image will be created and then posted
in the channel that the message came from.

Pillow:
    https://pillow.readthedocs.io/en/5.1.x/

Discord.py:
    https://github.com/Rapptz/discord.py
    Using the discord-rewrite.py docs:
        http://discordpy.readthedocs.io/en/rewrite/index.html

Github:
    https://github.com/Littlemansmg/Discord-Meme-Generator

"""

from MemeFormatting import *
from discord.ext import commands
from datetime import datetime as dt
import discord
import logging

logging.basicConfig(filename='discord.log', level = logging.INFO)

# memes that only use )top (top text only)
toplist = ['mocking-spongebob']

# memes that only use )bottom (bottom text only)
bottomlist = []

# memes that use )top )bottom )tb
# TODO: Make a list for top and bottom only memes?
topBottomList = [
    '10-guy', 'bad-luck-brian', 'good-guy-greg', 'roll-safe',
    'simply', 'successkid', 'willy-wonka', 'zucc']

# read token file
with open('token.txt') as token:
    token = token.readline()

# ---------------------------HELP------------------------------------

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
# ---------------------------Logs------------------------------------

def commandInfo(ctx):
    now = dt.now().strftime('%m/%d %H:%M ')
    logging.info(now + ' Command Used ' + ctx.message.server.name + ' ' + str(ctx.message.author)
                 + ' \'' + str(ctx.message.content) + ' \'')

def commandWarning(ctx):
    now = dt.now().strftime('%m-%d_%H:%M:%S')
    logging.warning(now + ' Meme Missing ' + ctx.message.server.name + ' ' + str(ctx.message.author) +
                    ' \'' + str(ctx.message.content) + ' \'')

# ---------------------------BOT-------------------------------------
bot = commands.Bot(command_prefix=')')

# execute when bot is logged in and ready
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('----------')
    # set what the bot is playing.
    await bot.change_presence(game = discord.Game(name = "Type )help for help"))

# execute if there is an error with a command.
@bot.event
async def on_command_error(error, ctx):
    # NOTE: It's stated in the documentation that CTX, should always be first.
    # for on_command_error, The first paramater is the error, and then the context
    # so error will always come first.
    destination = ctx.message.channel
    if isinstance(error, commands.MissingRequiredArgument):
        # LOG
        now = dt.now().strftime('%m/%d %H:%M ')
        server = ctx.server.name
        logging.error(now + str(error) + ' From: ' + ctx.message.server.name + ' ' +
                      str(ctx.message.author) + ' \'' + str(ctx.message.content) + ' \'')

        # send error to discord.
        await bot.delete_message(ctx.message)
        await bot.send_message(destination, "You are missing some arguments.")

# top and bottom command: )tb
@bot.command(pass_context=True, name='tb', description = "Prints top and bottom text.", help = tbhelp)
async def topAndBottom(ctx, memeType : str, topString : str, bottomString : str):
    # gets the channel and the message from the context.
    destination = ctx.message.channel
    message = ctx.message

    # deletes message that invoked the command.
    await bot.delete_message(message)

    # check if in proper list
    if memeType in topBottomList:
        send = top_bottom(memeType, topString, bottomString)
        await bot.send_file(destination, send)
        # LOG
        commandInfo(ctx)

    # Warning
    else:
        await bot.send_message(destination, "Sorry, " + memeType + " isn't available or not in this list.")
        # LOG
        commandWarning(ctx)

# top and bottom command: )top
@bot.command(pass_context = True, name = 'top',description = "Prints top atext.", help = tophelp)
async def topText(ctx, memeType, topString):
    # gets the channel and the message from the context.
    destination = ctx.message.channel
    message = ctx.message

    await bot.delete_message(message)

    # check if in proper list
    if memeType in toplist:
        send = top_bottom(memeType, topString, '')
        await bot.send_file(destination, send)
        # LOG
        commandInfo(ctx)

    # check if in proper list
    elif memeType in topBottomList:
        send = top_bottom(memeType, topString, '')
        await bot.send_file(destination, send)
        # LOG
        commandInfo(ctx)

    # Warning
    else:
        await bot.send_message(destination, "Sorry, " + memeType + " isn't available or not in this list.")
        # LOG
        commandWarning(ctx)

# top and bottom command: )bottom
@bot.command(pass_context = True, name = 'bottom',description = "Prints bottom text.", help = bottomhelp)
async def bottomText(ctx, memeType, bottomString):
    # gets the channel and the message from the context.
    destination = ctx.message.channel
    message = ctx.message

    await bot.delete_message(message)

    # check if in proper list
    if memeType in toplist:
        send = top_bottom(memeType, '', bottomString)
        await bot.send_file(destination, send)
        # LOG
        commandInfo(ctx)

    # check if in proper list
    elif memeType in topBottomList:
        send = top_bottom(memeType, '', bottomString)
        await bot.send_file(destination, send)
        # LOG
        commandInfo(ctx)

    # Warning
    else:
        await bot.send_message(destination, "Sorry, " + memeType + " isn't available or not in this list.")
        # LOG
        commandWarning(ctx)

# top and bottom command: )list
@bot.command(pass_context = True, name = 'list', description = "Prints a list of memes.", help = listhelp)
async def listMemes(ctx):
    # gets the channel and the message from the context.
    destination = ctx.message.channel
    message = ctx.message

    await bot.delete_message(message)

    # puts array's into a string form
    tmptop = ", ".join(toplist)
    tmpbottom = ", ".join(bottomlist)
    tmptb = ", ".join(topBottomList)

    await bot.send_message(destination, '```Top text only: ' + tmptop + '```')
    await bot.send_message(destination, '```Bottom text only: ' + tmpbottom + '```')
    await bot.send_message(destination, '```Top and Bottom text: ' + tmptb + '```')
    # LOG
    commandInfo(ctx)

# Start bot
bot.run(token.strip())
