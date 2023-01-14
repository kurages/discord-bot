from discord.ext.commands.context import Context
from discord.ext.commands import *

class Test(Cog):
	def __init__(self):
		self.text = "hi"

	@hybrid_command(name="test")
	async def excute(self, ctx:Context):
		await ctx.send(self.text)


