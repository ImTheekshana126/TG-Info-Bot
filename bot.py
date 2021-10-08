# Made with Python3
# (C) Vivek-TP and FayasNoushad

import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

Bot = Client(
        "Info Bot",
        bot_token = os.environ["BOT_TOKEN"],
        api_id = int(os.environ["API_ID"]),
        api_hash = os.environ["API_HASH"]
)

START_TEXT = """
<b>Hello {}

[bot](https://telegra.ph/file/536e97961e9870e718912.jpg)
"""
HELP_TEXT = """
🤔 How to use me?

• Forward a Message for take it's Details (in Private)

• Send any Media to take its Details (in private)

• Reply /info to a Message to take Message Details

• Use /info Command to take your Details

• Use /id in Group or Channel to get Unique Telegram ID
"""
ABOUT_TEXT = """
- **Bot :** `Info Bot`
- **Creator :** [Theekshana](https://telegram.me/ImTheekshana)
- **Credits :** `Everyone in this journey`
- **Source :** [Click here](https://github.com/)
- **Language :** [Python3](https://python.org)
- **Library :** [Pyrogram v1.2.0](https://pyrogram.org)
- **Server :** [Heroku](https://heroku.com)
"""

BOT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text="📜Source Code", url=f"https://github.com/ImTheekshana126/TG-Info-Bot")
        ]]
    )


START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text="Channel", url=f"t.me/theekshana_Official")
        ]]
    )
                
@Bot.on_message(filters.private & filters.command("start"))
async def start(bot, update):
    text = START_TEXT.format(update.from_user.mention) 
    reply_markup = START_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@Bot.on_message(filters.private & filters.command("help"))
async def help(bot, update):
    text = HELP_TEXT
    reply_markup = START_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )


@Bot.on_message(filters.private & filters.command("about"))
async def about(bot, update):
    text = ABOUT_TEXT
    reply_markup = START_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@Bot.on_message(filters.private & filters.command("info"))
async def info(bot, update):
    if update.from_user.last_name:
        last_name = update.from_user.last_name
    else:
        last_name = "None"
    text = f"""
**First Name :** {update.from_user.first_name}

** Your Second Name :** {last_name}

** Your Username :** {update.from_user.username}

** Your Telegram ID :** {update.from_user.id}

** Your Profile Link :** {update.from_user.mention}
""" 
    reply_markup = START_BUTTONS
    await update.reply_text(        
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@Bot.on_message(filters.private & filters.command("id"))
async def id(bot, update):
    text = f"""
**Your Telegram ID :** {update.from_user.id}
"""
    reply_markup = START_BUTTONS
    await update.reply_text(        
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

print(
    """
Bot Started!!! Now Join on @Theekshana_Support
"""
)

Bot.run()
