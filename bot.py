"""
Maintain, Telegram Maintain Bot

Copyright (C) 2021 Vivek-TP <https://t.me/unocy>
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
"""
import os
import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import pymongo

bot = Client(
    "Maintain-Bot",
    bot_token=os.environ["BOT_TOKEN"],
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"],
)

@bot.on_message(filters.command(["start", "help"]) | filters.text)
async def start_handler(client, message):
    user_mention = message.from_user.mention if message.from_user else ""
    response_message = f"Hai {user_mention}, This Bot Is Under Maintenance.\n\nYou Can't Use This Bot Right Now. " \
                       "You Will Get a Message On This Bot's Channel If This Bot Is Ready To Work."

    # Create InlineKeyboardMarkup with the specified buttons
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/botsxworld")],
        [InlineKeyboardButton("Dev", url="https://unocy.t.me")]
    ])

    await message.reply_text(response_message, reply_markup=keyboard)

# Start the bot
bot.run()
