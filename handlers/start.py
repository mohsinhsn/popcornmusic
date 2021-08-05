from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("https://telegra.ph/file/de160a8fa6ec59247e280.jpg")
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
\nI can play music in your
\ngroup's voice chat
Music Assistant - @popcornXhelper
\nTo add in your group contact us at @stylishUser
\nHit /help list of available commands.
 </b>""",
      
       
       reply_markup=InlineKeyboardMarkup(
           [
               [
                   InlineKeyboardButton(
                     "🎧Assistantbot", url="https://t.me/popcornXhelper",
                   )
               ],
               [
                   InlineKeyboardButton(
                       "💬 Help Group", url="https://t.me/StylishUser"
                   ),
                   InlineKeyboardButton(
                       "Chatting group", url="https://t.me/EnglishChatting_Club"
                   ),
                   InlineKeyboardButton(
                       "✨GitHub✨", url="http://www.github.com/mohsinHsn/popcornmusic"
                   )
               ],
               [
                   InlineKeyboardButton(
                       "➕ Add To Your Group ➕", url="https://t.me/popcornXplayerbot?startgroup=true"
                   ) 
               ]
           ]
       )
   )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Support Group  ", url="https://t.me/StylishUser"
                    )
                ],    
                [    
                    InlineKeyboardButton(
                        "Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
\n/play <song name> - play song you requested
/dplay <song name> - play song you requested via deezer
/splay <song name> - play song you requested via jio saavn
/playlist - Show now playing list
/current - Show now playing
/song <song name> - download songs you want quickly
/search <query> - search videos on youtube with details
/deezer <song name> - download songs you want quickly via deezer
/saavn <song name> - download songs you want quickly via saavn
/video <song name> - download videos you want quickly
\n*Admins only*
/player - open music player settings panel
/pause - pause song play
/resume - resume song play
/skip - play next song
/end - stop music play
/userbotjoin - invite assistant to your chat
/admincache - Refresh admin list
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Need Help❓", url="https://t.me/stylishuser"
                    )
                ]
            ]
        )
    )    
