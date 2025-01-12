# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from pyrogram import Client
import asyncio
from Music import SUDOERS as SUDO_USERS
from Music.config import GROUP as SUPPORT_GROUP
from pyrogram import filters
from pyrogram.types import Message
from Music import userbot as USER

PROJECT_NAME = "Joker Robot"
PMPERMIT = "ENABLE"
PMSET = True
pchats = []
OWNER = "@farizjs"

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    if PMPERMIT == "ENABLE" and PMSET:
        chat_id = message.chat.id
        if chat_id in pchats:
            return
        await USER.send_message(
            message.chat.id,
            f"Hello, I am **Service Assistant {PROJECT_NAME}.**\n\n ❗️ **Rules:**\n   - Don't Spam Order here\n   - Don't Spam Songs So There's No Error\n\n 👉 **SEND INVITE LINK OR GROUP USERNAME, IF ASSISTANT CANNOT JOIN YOUR GROUP.**\n\n ⛑ **Group Support :** @{SUPPORT_GROUP} - **Owner** {OWNER}\n\n",
        )
        return

    

@Client.on_message(filters.command(["/pmpermit"]))
async def bye(client: Client, message: Message):
    if message.from_user.id in SUDO_USERS:
        global PMSET
        text = message.text.split(" ", 1)
        queryy = text[1]
        if queryy == "on":
            PMSET = True
            await message.reply_text("**Pmpermit is turned on**")
            return
        if queryy == "off":
            PMSET = None
            await message.reply_text("**Permit is turned off**")
            return

@USER.on_message(filters.text & filters.private & filters.me)
async def autopmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if chat_id not in pchats:
        pchats.append(chat_id)
        await message.reply_text("Approved for Private Message")
        return
    message.continue_propagation()    
    
@USER.on_message(filters.command("yes", [".", ""]) & filters.me & filters.private)
async def pmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if chat_id not in pchats:
        pchats.append(chat_id)
        await message.reply_text("Approved for Private Message")
        return
    message.continue_propagation()    
    

@USER.on_message(filters.command("no", [".", ""]) & filters.me & filters.private)
async def rmpmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if chat_id in pchats:
        pchats.remove(chat_id)
        await message.reply_text("Sorry you were rejected for private message")
        return
    message.continue_propagation()
