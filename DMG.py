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
import asyncio
import discord
import logging
import unittest


logging.basicConfig(handlers = [logging.FileHandler('discord.log', 'a', 'utf-8')], level = logging.INFO)

# memes that only use )top (top text only)
toplist = ['mocking-spongebob']

# memes that only use )bottom (bottom text only)
bottomlist = []

# memes that use )top )bottom )tb
# TODO: Make a list for top and bottom only memes?
topBottomList = [
    '10-guy', 'bad-luck-brian', 'danger-zucc', 'good-guy-greg', 'roll-safe',
    'simply', 'successkid', 'willy-wonka', 'zucc']

# read token file
with open('token.txt') as token:
    token = token.readline()

# ---------------------------HELP------------------------------------

listhelp = 'Prints a list of all the memes available.'

tbhelp = 'Prints top and bottom text memes.\n' \
         'Notes: This command can only be used with memes that are in the Top and Bottom List. ' \
         '\nTEXT MUST BE IN SINGLE OR DOUBLE QUOTES.\n' \
         'Example: )tb simply "One does not simply" "Program and not hate themselves"'

tophelp = 'Prints top text memes.\n' \
          'Notes: This command will only print toptext. It can only be used with memes that are in the Top List ' \
          'or Top and Bottom list.\n' \
          'Example: )top mocking-spongebob I\'m an example sentence'

bottomhelp = 'Prints bottom text memes.\n' \
             'Notes: This command will only print bottomtext. It can only be used with memes that are in the ' \
             'Bottom List or Top and Bottom list.\n' \
             'Example: )bottom roll-safe This isn\'t the correct format, but it works.'

suggesthelp = 'Sends a suggestion to the dev.\n' \
              'Notes: This command will send all suggestions to the developer of the bot. ' \
              'Feel free to suggest meme templates, features, or report any bugs here.\n' \
              'Example: )suggest Hey dev, get your shit together and add more memes.'

viewallhelp = 'Sends the user a template.\n' \
              'Notes: This command will PM the user a list of all available memes to choose from.\n' \
              'Example: )viewall '

viewallTop = 'Sends the user a template.\n' \
             'Notes: This command will PM the user a list of all available memes to choose from.\n' \
             'Example: )viewall top '

viewallTb = 'Sends the user a template.\n' \
            'Notes: This command will PM the user a list of all available memes to choose from.\n' \
            'Example: )viewall tb '

viewallBottom = 'Sends the user a template.\n' \
                'Notes: This command will PM the user a list of all available memes to choose from.\n' \
                'Example: )viewall bottom '

viewallMeme = 'Sends the user a template.\n' \
              'Notes: This command will PM the user a list of all available memes to choose from.\n ' \
              'Example: )viewall meme 10-guy '

devhelp = 'Provides notes and info from the dev.\n' \
          'Notes: This command is just to print out the dev\'s notes/thoughts.\n' \
          'Example: )dev'

# ---------------------------Logs------------------------------------

def commandInfo(ctx):
    now = dt.now().strftime('%m/%d %H:%M ')
    logging.info(now + ' Command Used: '
                 + ' Server: ' +ctx.message.server.name + ':' + ctx.message.server.id
                 + ' Author: ' + str(ctx.message.author)
                 + ' Invoke: \'' + str(ctx.message.content) + ' \'')

def commandWarning(ctx):
    now = dt.now().strftime('%m-%d_%H:%M:%S')
    logging.warning(now + ' Meme Missing.'
                    + ' Server: ' + ctx.message.server.name + ':' + ctx.message.server.id
                    + ' Author: ' + str(ctx.message.author)
                    + ' Invoke: \'' + str(ctx.message.content) + ' \'')

def masterWarning(ctx):
    now = dt.now().strftime('%m/%d %H:%M ')
    logging.info(now + ' Command Used: '
                 + ' Server: ' + ctx.message.server.name + ':' + ctx.message.server.id
                 + ' Author: ' + str(ctx.message.author)
                 + ' Invoke: \'' + str(ctx.message.content) + ' \'')

# ---------------------------Checks----------------------------------

def is_owner_check():
    def predicate(ctx):
        return ctx.message.author.id == '179050708908113920'
    return commands.check(predicate)

def is_admin_check():
    def predicate(ctx):
        return ctx.message.author.discord.Permissions.administrator
    return commands.check(predicate)

def oofSettingOn():
    with open('command settings/oof.txt') as oof:
        bool = oof.readline()
    return bool

pass
# ---------------------------BOT-------------------------------------
bot = commands.Bot(command_prefix=')')

# execute when bot is logged in and ready
@bot.event
async def on_ready():
    await bot.change_presence(game = discord.Game(name = "Type )help for help"))

@bot.event
async def on_message(message):
    bool = oofSettingOn()
    content = message.content
    if content.lower().startswith('oof') and bool.strip() == 'True':
        await bot.delete_message(message)

        await bot.send_file(message.channel, 'command settings/oof.jpg')

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
        logging.error(now + str(error)
                      + ' Server: ' + ctx.message.server.name + ':' + ctx.message.server.id
                      + ' Author: ' + str(ctx.message.author)
                      + ' Invoke: \'' + str(ctx.message.content) + ' \'')

        # send error to discord.
        await bot.delete_message(ctx.message)
        await bot.send_message(destination, "You are missing some arguments.")

# Invoke: )tb <memetype> <topstring> <bottomstring>
@bot.command(pass_context=True, name='tb', description = "Prints top and bottom text.", help = tbhelp)
#@maxChar()
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

@topAndBottom.error
async def topandbottom_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        destination = ctx.message.channel
        await bot.send_message(destination, 'Sorry. Only 35 characters allowed to keep the meme looking good.')

# Invoke: )top <memetype> <topstring>
@bot.command(pass_context = True, name = 'top',description = "Prints top text.", help = tophelp)
#@maxChar()
async def topText(ctx, memeType, *, topString):
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

@topText.error
async def topText_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        destination = ctx.message.channel
        await bot.send(destination, 'Sorry. Only 35 characters allowed to keep the meme looking good.')

# Invoke: )bottom <memetype> <bottomstring>
@bot.command(pass_context = True, name = 'bottom',description = "Prints bottom text.", help = bottomhelp)
#@maxChar()
async def bottomText(ctx, memeType, *, bottomString):
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

@bottomText.error
async def bottomText_error(error, ctx):
    if isinstance(error, commands.CheckFailure):
        destination = ctx.message.channel
        await bot.send(destination, 'Sorry. Only 35 characters allowed to keep the meme looking good.')

# Invoke: )list
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

# Invoke: )suggest <suggestion>
@bot.command(pass_context = True, name = 'suggest', description = "Sends the Bot Dev a suggestion.", help = suggesthelp)
async def suggest(ctx, *, suggestion):
    # gets the channel and the message from the context.
    destination = ctx.message.channel
    message = ctx.message

    await bot.delete_message(message)

    # writes suggestion to a file
    with open('suggest.txt', 'a') as suggest:
        now = dt.now().strftime('%m/%d %H:%M ')
        suggest.write(now + " " + str(ctx.message.author) + ' Suggestion: ' + suggestion + "\n")

    await bot.send_message(destination, 'Your suggestion has been recorded.')

    # Notifies specifically LittlemanSMG#6041 of any suggestion made
    owner = discord.utils.get(bot.get_all_members(), id = '179050708908113920')
    await bot.send_message(owner, 'Suggestion made. Check suggest.txt.')

    #LOG
    commandInfo(ctx)

# Invoke: )viewall
@bot.group(pass_context = True, name = 'viewall', description = "Display templates.", help = viewallhelp)
async def viewall(ctx):
    message = ctx.message

    await bot.delete_message(message)

    if ctx.invoked_subcommand is None:
        # send all memes to user via PM
        await bot.send_message(ctx.message.author, "Top and Bottom Text.")

        for tb in topBottomList:
            await bot.send_message(ctx.message.author, tb + ":")
            await bot.send_file(ctx.message.author, 'Templates/' + tb + '.jpg')

        await bot.send_message(ctx.message.author, "Top Text.")

        for top in toplist:
            await bot.send_message(ctx.message.author, top + ":")
            await bot.send_file(ctx.message.author, 'Templates/' + top + '.jpg')

        await bot.send_message(ctx.message.author, "Bottom Text.")

        for bottom in bottomlist:
            await bot.send_message(ctx.message.author, bottom + ":")
            await bot.send_file(ctx.message.author, 'Templates/' + bottom + '.jpg')

        #LOG
        commandInfo(ctx)

# Invoke )viewall top
@viewall.command(pass_context = True, name = 'top', help = viewallTop )
async def _top(ctx):
    # send all toplist memes to user via PM
    for meme in toplist:
        await bot.send_message(ctx.message.author, meme + ":")
        await bot.send_file(ctx.message.author, 'Templates/' + meme + '.jpg')

    #LOG
    commandInfo(ctx)

# Invoke )viewall tb
@viewall.command(pass_context = True, name = 'tb', help = viewallTb)
async def _tb(ctx):
    # send all topBottomlist memes to user via PM
    for meme in topBottomList:
        await bot.send_message(ctx.message.author, meme + ":")
        await bot.send_file(ctx.message.author, 'Templates/' + meme + '.jpg')

    #LOG
    commandInfo(ctx)

# Invoke )viewall bottom
@viewall.command(pass_context = True, name = 'bottom', help = viewallBottom)
async def _top(ctx):
    # send all bottomlist memes to user via PM
    for meme in bottomlist:
        await bot.send_message(ctx.message.author, meme + ":")
        await bot.send_file(ctx.message.author, 'Templates/' + meme + '.jpg')

    #LOG
    commandInfo(ctx)

# Invoke )viewall meme <meme>
@viewall.command(pass_context = True, name = 'meme', help = viewallMeme)
#@maxChar()
async def _view(ctx, meme):
    # send specific meme template to user via PM
    if meme in toplist or meme in topBottomList or meme in bottomlist:
        await bot.send_message(ctx.message.author, meme + ":")
        await bot.send_file(ctx.message.author, 'Templates/' + meme + '.jpg')
        # LOG
        commandInfo(ctx)

    else:
        await bot.send_message(ctx.message.author, "Can't find meme: " + meme)
        #LOG
        commandWarning(ctx)

@bot.command(pass_context = True, name = 'dev', description = 'Prints dev notes', help = devhelp)
async def dev(ctx):
    # gets the channel and the message from the context.
    destination = ctx.message.channel
    message = ctx.message

    await bot.delete_message(message)

    notes = '```' \
            'Author: Scott "LittlemanSMG" Goes.\n' \
            'Language: Python.\n\n' \
            'Notes about Generation-Meme: It only supports bottom and top text memes. This is because ' \
            'I\'m lazy and I need to learn how to format each meme. If you want to help, leave a' \
            'suggestion and I will get in contact with you.\n\n' \
            'LOGGING: I\'m currently keeping logs of my bot usage. Log format goes as follows;\n' \
            '  <date> <server_name> <server_ID> <Username#0000> <command used>\n' \
            '```'
    await bot.send_message(destination, notes)

@bot.command(pass_context = True, name = 'master', hidden = True)
@is_owner_check()
async def personalCommand(ctx, *, announcement):
    destination = ctx.message.channel
    message = ctx.message

    await bot.delete_message(message)

    await bot.send_message(destination, '```' + announcement + '```')

@personalCommand.error
async def personalCommand_error(error, ctx):
    destination = ctx.message.channel
    message = ctx.message

    await bot.delete_message(message)

    await bot.send_message(destination, "Fuck you. *How do you even know this command exists?*")
    masterWarning(ctx)

@bot.command(pass_context = True, name = 'oof', description = 'Turns oof on or off')
@is_admin_check()
async def oofSetting(ctx):
    destination = ctx.message.channel
    message = ctx.message
    ison = oofSettingOn()

    await bot.delete_message(message)

    if ison == 'True':
        with open('command settings/oof.txt', ) as oof:
            oof.write('False')

        await bot.send_message(destination, "oof setting is now off.")

    else:
        with open('command settings/oof.txt') as oof:
            oof.write('True')

        await bot.send_message(destination, "oof setting is now off.")

#test: bot doesn't turn off randomly
try:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bot.run(token.strip()))
except:
    print ('This is probably a Runtime error from turning me off.')
