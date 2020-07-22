"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
#IMG CREDITS: @WhySooSerious
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"
ALIVE_IMG = "https://telegra.ph/file/a34493e9d843193edb7d5.jpg"
ALIVE_caption = "`Pikachu Is:` **𝑶𝒏𝒍𝒊𝒏𝒆**\n"
ALIVE_caption += "**System Status **\n"
ALIVE_caption += "`Telethon Version:` **6.0.9**\n`Python:` **3.7.4**\n"
ALIVE_caption += "`Data Servers :` **Functioning**\n"
ALIVE_caption += "**Current Branch** : `master`\n"
ALIVE_caption += "**PikaOS** : `1.0 Beta`\n"
ALIVE_caption += f"**My Peru Owner** : {DEFAULTUSER} \n"
ALIVE_caption += "**Heroku Database** : `AWS - Working Properly`\n"
ALIVE_caption += "Copyright By [ItzSjDude](t.me/ItzSjDude)\n"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.delete() 
    await borg.send_file(alive.chat_id, ALIVE_IMG,caption=ALIVE_caption)
