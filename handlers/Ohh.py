 
from pyrogram import *
from pyrogram.types import *
from helpers.basic import edit_or_reply
from main import SUDOERS
import asyncio

 
 

@Client.on_message(filters.command(["oh", "ohh"], [".", "!"]) & filters.user(SUDOERS)) 
async def hello_world(client: Client, message: Message):
    mg = await edit_or_reply(message, "oh")
    await asyncio.sleep(0.2)
    await mg.edit("oohh")
    await asyncio.sleep(0.2)
    await mg.edit("oohhh")
    await asyncio.sleep(0.2) 
    await mg.edit("oohhhh")
    await asyncio.sleep(0.2) 
    await mg.edit("oohhhhh")
    await asyncio.sleep(0.2) 
    await mg.edit("oohhhhhh") 
    await asyncio.sleep(0.2) 
    await mg.edit("oohhhhhhh") 
    await asyncio.sleep(0.2) 
    await mg.edit("oohhhhhhhh")



