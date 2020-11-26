import discord
from discord.ext import commands

def setup(bot):
	bot.add_cog(CommandesBasiques(bot))

class CommandesBasiques(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def coucou(self, ctx):
		await ctx.send("Coucou !")
		await ctx.send("Comment allez vous ?")
