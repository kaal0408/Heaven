from pyrogram import filters
from pyrogram import __version__ as pyro_vr
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from main import *
from pyrogram import Client
from main import ALIVE_PIC
 

@Client.on_message(filters.command(["alive", "awake"], [".", "!"]) & filters.user(SUDOERS))
async def alive(client: Client, e: Message):
    ids = 0
    try:
        if bot:
            ids += 1
        if bot1:
            ids += 1
        Alive_msg = f"нεαvεη υsεявσт ιs αℓιvε 🔥 \n\n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n"
        Alive_msg += f"► vεяsιση : `Beta.0.1` \n"
        Alive_msg += f"► ρүяσ vεяsιση : `{pyro_vr}` \n"
        Alive_msg += f"► αcтιvε ι∂s : `{ids}` \n"
        Alive_msg += f"► sυρρσят : [Jᴏɪɴ.](https://t.me/Murat_30_God) \n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n\n"
        await e.reply_photo(
        photo=ALIVE_PIC,
        caption=Alive_msg,
        reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton(
                        "• 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 •", url="https://t.me/Murat_30_God")
                ], [
                    InlineKeyboardButton(
                        "• 𝐑𝐞𝐩𝐨 •", url="https://github.com/kaal0408/Heaven-USERBOT")
                ]],
        ),
    ) 
    except Exception as lol:         
        Alive_msg = f"нεαvεη υsεявσт ιs αℓιvε🔥 \n\n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n"
        Alive_msg += f"► vεяsιση : `Beta.0.1` \n"
        Alive_msg += f"► ρүяσ vεяsιση : `2.0.5` \n"
        Alive_msg += f"► sυρρσят : [Jᴏɪɴ](https://t.me/Murat_30_God) \n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n\n"
        await e.reply_photo(
        photo=ALIVE_PIC,
        caption=Alive_msg,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• Channel •", url="https://t.me/Murat_30_God"),
                ],
                [
                    InlineKeyboardButton("• Repo •", url="https://github.com/kaal0408/Heaven-Userbot"),
                ],
            ],
        ),
    ) 

