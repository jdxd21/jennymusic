from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from ZedzeX import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@app.on_message(
    filters.command("owner")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/9d7c2a95c8f102fb4f48f.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐃𝐌❤️𝐎𝐖𝐍𝐄𝐑🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "〖°𝑱𝑬𝑵𝑵𝒀 𝑿 𝑴𝑼𝑺𝑰𝑪 🦋💙°〗", url=f"https://t.me/JAI_NISH_21")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("owner")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/9d7c2a95c8f102fb4f48f.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐃𝐌❤️𝐎𝐖𝐍𝐄𝐑🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "〖°𝑱𝑬𝑵𝑵𝒀 𝑿 𝑴𝑼𝑺𝑰𝑪 🦋💙°〗", url=f"https://t.me/JAI_NISH_21")
                ]
            ]
        ),
    )


@app.on_message(
    filters.command("katil")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/9d7c2a95c8f102fb4f48f.jpg",
        caption=f"""🦋•────────────────•🦋 \n          🇸𝗧𝗨𝗗𝗬  𝙉𝘿 𝘾𝙍𝙔😭
🦋•────────────────•🦋
┏━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━━━┓

𝐌𝗢𝐇𝗔𝐁𝗕𝐀𝗧 𝐇𝗢 𝐆𝗔𝐘𝗜 𝐓𝗛𝐈 𝐃𝗢𝐍𝗢 𝐊𝗢[ Sᴛᴜᴅʏ ɴᴅ ᴍᴇ ] 𝐄𝗞 𝐀𝗥S𝗔 𝐇𝗢 𝐆𝗬𝐀
👉👈 𝐌𝗘𝐑𝗔 𝐘𝗘 𝐈𝗦𝐇𝗤 𝐓𝗛𝐀 𝐃𝗢 𝐓𝗔𝐑𝗙𝐀 𝐄𝗞 𝐓𝗔𝐑𝗙𝐀 𝐇𝗢 𝐆𝗔𝐘𝗔❤️😭🦋😂

┗━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━┛""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Sᴀʏᴀʀɪ Lᴏᴠᴇʀs✨❤️🥀", url=f"https://t.me/JENNY_CHATS")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("katil")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/9d7c2a95c8f102fb4f48f.jpg",
        caption=f"""🦋•────────────────•🦋 \n          🇸𝗧𝗨𝗗𝗬  𝙉𝘿 𝘾𝙍𝙔😭
🦋•────────────────•🦋
┏━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━━━┓

𝐌𝗢𝐇𝗔𝐁𝗕𝐀𝗧 𝐇𝗢 𝐆𝗔𝐘𝗜 𝐓𝗛𝐈 𝐃𝗢𝐍𝗢 𝐊𝗢[ Sᴛᴜᴅʏ ɴᴅ ᴍᴇ ] 𝐄𝗞 𝐀𝗥S𝗔 𝐇𝗢 𝐆𝗬𝐀
👉👈 𝐌𝗘𝐑𝗔 𝐘𝗘 𝐈𝗦𝐇𝗤 𝐓𝗛𝐀 𝐃𝗢 𝐓𝗔𝐑𝗙𝐀 𝐄𝗞 𝐓𝗔𝐑𝗙𝐀 𝐇𝗢 𝐆𝗔𝐘𝗔❤️😭🦋😂

┗━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━┛""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Sᴀʏᴀʀɪ Lᴏᴠᴇʀs✨❤️🥀", url=f"https://t.me/JENNY_CHATS")
                ]
            ]
        ),
    )


@app.on_message(
    filters.command("repo")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/9d7c2a95c8f102fb4f48f.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐆𝐄𝐓🌱𝐑𝐄𝐏𝐎🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌱ƨσʋяcɛ🌱", url=f"DM ME 🦋💓https://t.me/JAI_NISH_21")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("source")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/9d7c2a95c8f102fb4f48f.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐆𝐄𝐓🌱𝐑𝐄𝐏𝐎🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌱ƨσʋяcɛ🌱", url=f"DM ME 🦋💓https://t.me/JAI_NISH_21")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("repo")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/9d7c2a95c8f102fb4f48f.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐆𝐄𝐓🌱𝐑𝐄𝐏𝐎🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌱ƨσʋяcɛ🌱", url=f"DM ME 🦋💓 https://t.me/JAI_NISH_21")
                ]
            ]
        ),
    )
