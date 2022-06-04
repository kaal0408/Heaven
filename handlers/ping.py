from datetime import datetime
from pyrogram import Client
from pyrogram import filters
from main import *
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

ms = "Heaven user"

@Client.on_message(filters.command(["ping", "Ping"], [".", "!"]) & filters.user(SUDOERS))
async def ping(_, message: Message):
    await message.reply_text(f"""⭐ **
╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱
┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱
┃╰━╯┃╭━━╮╭━━╮╭━━╮
┃╭━━╯┃╭╮┃┃╭╮┃┃╭╮┃
┃┃╱╱╱┃╰╯┃┃┃┃┃┃╰╯┃
╰╯╱╱╱╰━━╯╰╯╰╯╰━╮┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯
** ⭐MY MS → `{ms}`\n """)


#credit goes to astro userbot
#made by Loverboyxd
 
