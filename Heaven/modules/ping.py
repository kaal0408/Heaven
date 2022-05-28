import asyncio
import random
from datetime import datetime

from pyrogram.types import Message

from asterix import app, gen

app.CMD_HELP.update(
    {
        "ping": (
            "ping",
            {
                "ping": "Shows you the response speed of the bot.",
                "ping [ number ]": "Make infinite pings, don't overuse.",
            },
        )
    }
)


# animations
data = ["🕜", "🕡", "🕦", "🕣", "🕥", "🕧", "🕓", "🕔", "🕒", "🕑", "🕐"]

pings = []
pings.clear()


@app.on_message(gen(["ping", "pong"], allow=["sudo", "channel"]))
async def ping(_, msg: Message):
    st = time.time()
    et = time.time()
    mention = msg.from_user.mention
    uptime = f"\n`{round((et - st), 3)} ms`"
    textt = """
★°:･✧*.°☆.*★°●¸★　 
▃▃▃▃▃▃▃▃▃▃▃
┊ ┊ ┊ ┊ ┊ ┊┊
┊ ┊ ┊ ┊ ˚✩ ⋆｡˚ ✩
┊ ┊ ┊ ┊⍣∙°⚝○｡°✯
┊ ┊ ┊ ┊
┊ ┊ ┊ ⛦『P‌๏‌и‌ɠ‌』 
┊ ┊ ┊︎✫ ˚♡ ⋆˚ ⋆｡ ❀
┊ ┊ ┊
┊ ┊ ┊𓆩𝙈𝙎--≻{} ﮩ٨ـﮩﮩ٨ـ𓆪
┊ ┊ ✯
┊ ✬ ˚•˚✩
┊⍣ •°
┊亗•ʍʏ ๏ωиэя•亗
★• {} •

⚘ Heaven Bot ⚘
""".format(uptime, mention)
    await msg.edit(textt)
#all credit goes to Astroub
