import time
from main import SUDOERS
from pyrogram import filters, Client
from pyrogram.errors import UserAdminInvalid
from pyrogram.types import Message, ChatPermissions

from helpers.PyroHelpers import GetUserMentionable
from helpers.adminHelpers import CheckAdmin, CheckReplyAdmin, RestrictFailed





@Client.on_message(filters.command("kick", ".") & filters.user(SUDOERS))
async def kick_user(bot: Client, message: Message):
    if await CheckReplyAdmin(message) and await CheckAdmin(message):
        try:
            mention = GetUserMentionable(message.reply_to_message.from_user)

            await bot.kick_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id,
            )

            await message.edit(f"Goodbye, {mention}.")
        except UserAdminInvalid:
            await RestrictFailed(message)



