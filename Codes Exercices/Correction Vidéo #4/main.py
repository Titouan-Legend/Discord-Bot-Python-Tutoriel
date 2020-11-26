import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!", description = "Bot de Titouan")

@bot.event
async def on_ready():
	print("Ready !")

@bot.command()
async def bansId(ctx):
	ids = []
	bans = await ctx.guild.bans()
	for i in bans:
		ids.append(str(i.user.id))
	await ctx.send("La liste des id des utilisateurs bannis du serveur est :")
	await ctx.send("\n".join(ids))

bot.run("NzA3Njc4MjI1MDA1OTM2NjUy.Xr6t8A.nZ_INNn_Xl-BuRcZ-qRGwiPqVXU")