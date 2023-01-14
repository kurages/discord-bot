import discord
from discord import app_commands
from discord.ext import commands

from .config import *
from .commands import COMMAND_LIST

class Bot(commands.Bot):
	def __init__(self) -> None:
		# intents = discord.Intents.default()
		intents = discord.Intents.all()
		intents.message_content = True
		super().__init__(command_prefix=COMMAND_PREFIX, intents=intents)

	async def load(self):
		for i in COMMAND_LIST:
			await self.add_cog(i())

	async def on_ready(self):
		await self.load()
		await self.tree.sync()
		print(f'Logged on as {self.user}!')

	async def on_message(self, message):
		print(f'Message from {message.author}: {message.content}')
		await self.process_commands(message)


