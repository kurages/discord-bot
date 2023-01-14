
import os
from os.path import join, dirname

from dotenv import load_dotenv

from src.bot import Bot

load_dotenv(".env", verbose=True)

bot = Bot()
bot.run(os.environ.get("TOKEN"))

