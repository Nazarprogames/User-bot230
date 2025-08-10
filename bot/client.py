from telethon import TelegramClient
from .config import API_ID, API_HASH, SESSION
client = TelegramClient(SESSION, API_ID, API_HASH)