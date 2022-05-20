import asyncio

from pyrogram.types import Message

from Pyrogram import Client



@Client.on_message(filters.command(["quote"]))
async def quotly_handler(_, m: Message):
    reply = m.reply_to_message
    if not reply:
        return await app.send_edit(m, "Reply to any users text message", delme=4)

    m = await app.send_edit(m, "Making a Quote . . .", text_type=["mono"])
    await reply.forward("@QuotLyBot")
    is_sticker = True
    while is_sticker:
        try:
            msg = await app.get_last_msg(message=m, chat_id="@QuotLyBot", limit=1)
            msg[0]["sticker"]["file_id"]
            is_sticker = False
        except:
            await asyncio.sleep(0.5)
    if msg_id := msg[0]["message_id"]:
        await asyncio.gather(
            m.delete(), app.copy_message(m.chat.id, "@QuotLyBot", msg_id)
        )
