#  szrosebot only

import os
import pyrogram
from pyrogram import Client, filters
import YoutubeTags 
from YoutubeTags import videotags
from DewmiBot import pbot 
from DewmiBot.events import register

@register(pattern="^/tags$")
async def virusscan(event):
    tags = videotags(link) 
    await message.reply_text("**These are the Tags that I Found** \n\n ` {tags} `"
    
