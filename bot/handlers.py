from telethon import events
from .client import client
from utils.logger import logger

@client.on(events.NewMessage(outgoing=True, pattern=r"^/.ping$"))
async def ping(event):
    await event.reply("pong")