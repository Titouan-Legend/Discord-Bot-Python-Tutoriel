import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix = "!", description = "Bot de Titouan")

@bot.event
async def on_ready():
	print("Ready !")

@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, user : discord.User, *reason):
	reason = " ".join(reason)
	await ctx.guild.ban(user, reason = reason)
	await ctx.send(f"{user} à été ban pour la raison suivante : {reason}.")

def isOwner(ctx):
	return ctx.message.author.id == 441881039338471425

@bot.command()
@commands.check(isOwner)
async def private(ctx):
	await ctx.send("Cette commande peut seulement etre effectuées par le propriétaire du bot !")

	
bot.run("NzA3Njc4MjI1MDA1OTM2NjUy.XsbN8g.n4ZnavWhgkEpuPzja_8i2BzvupY")
