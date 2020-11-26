import discord
from discord.ext import commands

class CogOwner(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	async def cog_check(self, ctx):
		return ctx.author.id == 441881039338471425


	def mon_check(ctx):
		return ctx.message.channel.id == 727201195214635029

	@commands.command()
	@commands.check(mon_check)
	async def admin(self, ctx):
		await ctx.send("Cette fonction est seulement disponible pour le propriétairee.")
