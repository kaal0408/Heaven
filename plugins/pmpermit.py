import os 
from pyrogram import Client
import asyncio
from config import OWNER_IDS
from config import PMPERMIT
from pyrogram import filters
from pyrogram.types import Message
from helper import client as USER
from pyrogram.types import Message, Voice, InlineKeyboardButton, InlineKeyboardMarkup

OWNER_USERNAME = os.environ.get("OWNER_USERNAME", None)
if "@" in master_user:
    master_user.replace("@", "")

PMSET =True
pchats = []

@USER.on_message(filters.text & filters.private & ~filters.me )
async def pmPermit(client: USER, message: Message):
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="⚜ Master ⚜", url=f"https://t.me/{OWNER_USERNAME}")   
            ]
        ]
    )
    if PMPERMIT == "ENABLE":
        if PMSET:
            chat_id = message.chat.id
            if chat_id in pchats:
                return
            await message.reply_photo(
                photo="https://telegra.ph/file/86336252ab3c5125c2a6b.jpg",
                reply_markup=keyboard,
                caption="This Is Pyrogram Assistant For {OWNER_USERNAME} ",
            )
            return

    

@Client.on_message(filters.command([".pmpermit"]))
async def bye(client: Client, message: Message):
    if message.from_user.id in OWNER_IDS:
        global PMSET
        text = message.text.split(" ", 1)
        queryy = text[1]
        if queryy == "on":
            PMSET = True
            await message.reply_text("PM Permit Enabled")
            return
        if queryy == "off":
            PMSET = None
            await message.reply_text("PM Permit Disabled")
            return

@USER.on_message(filters.text & filters.private & filters.me)        
async def autopmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("Auto Approved ...")
        return
    message.continue_propagation()    
    
@USER.on_message(filters.command("a", [".", ""]) & filters.me & filters.private)
async def pmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("Approoved to PM")
        return
    message.continue_propagation()    
    

@USER.on_message(filters.command("da", [".", ""]) & filters.me & filters.private)
async def rmpmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if chat_id in pchats:
        pchats.remove(chat_id)
        await message.reply_text("Dispprooved to PM")
        return
    message.continue_propagation()
