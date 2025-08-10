from bot.client import client
from utils.logger import logger
from bot import handlers  

if __name__ == "__main__":
    logger.info("Starting userbot…")
    client.start()                 
    client.run_until_disconnected()