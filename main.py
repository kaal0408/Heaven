import requests
from pyrogram import idle
from pyrogram import Client as Bot

from config import API_ID, API_HASH, OWNER_IDS


bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    plugins=dict(root="plugins")
)

bot.start()
run()
idle()
