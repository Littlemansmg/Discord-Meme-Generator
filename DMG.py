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

toplist = []
bottomlist = []

topBottomList = [
    '10-guy', 'bad-luck-brian', 'good-guy-greg', 'mocking-spongebob', 'roll-safe',
    'simply', 'successkid', 'willy-wonka']

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

@bot.event
async def on_command_error(error, ctx):
    # NOTE: It's stated in the documentation that CTX, should always be first.
    # for on_command_error, The first paramater is the error, and then the context
    # so error will always come first.
    destination = ctx.message.channel
    if isinstance(error, commands.MissingRequiredArgument):
        await bot.delete_message(ctx.message)
        await bot.send_message(destination, "You are missing some arguments.")

@bot.command(pass_context=True, name='tb')
async def topAndBottom(ctx, memeType, topString, bottomString):
    destination = ctx.message.channel
    message = ctx.message

    await bot.delete_message(message)

    if memeType in topBottomList:
        send = top_bottom(memeType, topString, bottomString)
        await bot.send_file(destination, send)

    else:
        await bot.send_message(destination, "Sorry @" + str(ctx.message.author) + ", " + memeType + " isn't here.")

@bot.command(pass_context = True, name = 'top')
async def topText(ctx, memeType, topString):
    destination = ctx.message.channel
    message = ctx.message

    await bot.delete_message(message)

    if memeType in toplist:
        send = top_bottom(memeType, topString, '')
        await bot.send_file(destination, send)

    elif memeType in topBottomList:
        send = top_bottom(memeType, topString, '')
        await bot.send_file(destination, send)

@bot.command(pass_context = True, name = 'bottom')
async def bottomText(ctx, memeType, bottomString):
    destination = ctx.message.channel
    message = ctx.message

    await bot.delete_message(message)

    if memeType in toplist:
        send = top_bottom(memeType, '', bottomString)
        await bot.send_file(destination, send)

    elif memeType in topBottomList:
        send = top_bottom(memeType, '', bottomString)
        await bot.send_file(destination, send)

@bot.command(pass_context = True, name = 'help')
async def help(ctx):
    destination = ctx.message.channel
    message = ctx.message

    listhelp = [toplist, bottomlist, topBottomList]
    tbhelp = '''\n
    )tb <memetype> <"top text"> <"bottom text"> - Notes: this command can only be used with memes
    that are in the Top and Bottom List. Text must be in single or double quotes.\n
    '''
    tophelp = '''\n
    )top <memetype> <"toptext"> - Notes: This command will only print toptext. It can only be used
    with memes that are in the Top List or Top and Bottom list. Text must be in single or double quotes.\n
    '''
    bottomhelp = '''\n
    )bottom <memetype> <"bottomtext"> - Notes: This command will only print bottomtext. It can only be used
    with memes that are in the Bottom List or Top and Bottom list. Text must be in single or double quotes.\n
    '''

    await bot.send_message(destination, (tbhelp, tophelp, bottomhelp))

bot.run(token)
