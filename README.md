# Discord-Meme-Generator
This program is built to allow discord users to type a command and then fill in top/bottom text. 
This image will be created and then posted in the channel that the message came from.

## Getting Started
I'm currently working on making the bot public, but if you want to make changes yourself or selfhost here is what you can do:

### Requirements
* Bot needs a user acount. (Don't ask me how to do this, tutorials are everywhere)
* Python 3 needs to be installed on whatever device is hosting the bot.
* Impatct font `impact.ttf` must be installed on whatever device is hosting the bot.

### Instructions
* Download the source code.
* Change `bot.run(token.strip())` to `bot.run('YOUR TOKEN HERE')`
* Powershell
  * cd into the folder where `DMG.py` is located.
  * type `python DMG.py` 
  * bot is running.
* Linux
  * cd into the folder where `DMG.py` is located.
  * type `python3 DMG.py`
    * Note: type `python3 DMG.py &` to run the bot in the background.
  * bot is running.

## Current Functionality
* Bot can send memes to discord.
* Bot can send memes through PM.
* Users can suggest edits to the bot that the owner will see.
* Bot will not crash under user inputs.
* Log will be created upon usage or predefined error.

## TODO
*This list is in no particular order.*
* More meme templates.
  * This requires formatting that is a big project.
* Set char limit.
  * This is to keep the memes looking nice.
* Limit command usage?
  * This is to deter spammers. All the commands will go, but it takes a while.
* Get meme templates by file name
  * This is so that if I add more memes, I don't have to classify them myself.
* Text Wrapping.
  * This can eliminate the need for a smaller char limit, but I have no idea where to begin with it.

### Extras
* Have server specific settings
  * This could be from turning off max chars to disallowing memetypes.
* Admin/role specific commands
  * This would tie into specific settings so not everybody can turn stuff off. 

## Built With
* [Discord.py](https://github.com/Rapptz/discord.py) - Discord API wrapper to run a discord bot in Python.
  * Note: This includes stuff from [discord-rewrite.py](https://discordpy.readthedocs.io/en/rewrite/index.html)
  , and discord.py. Both Documents were used in the creation of the bot.
* [Pillow](https://pillow.readthedocs.io/en/3.0.x/index.html) - Image formatting tool used to create the memes.

## Commands
* `)top <memetype> <string>`
* `)bottom <memetype> <string>`
* `)tb <memetype> <"string"> <"string">`
* `)list`
* `)viewall`
* `)viewall top`
* `)viewall bottom`
* `)viewall tb`
* `)viewall <memetype>`
* `)suggest <string>`
* `)dev`
* `)help`
