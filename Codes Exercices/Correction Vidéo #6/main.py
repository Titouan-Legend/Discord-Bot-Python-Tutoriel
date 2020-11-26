import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix = "!", description = "Bot de Titouan")

@bot.event
async def on_ready():
	print("Ready !")

def isPair(ctx):
	return ctx.message.author.id % 2 == 0

@bot.command()
@commands.check(isPair)
@commands.has_permissions(manage_messages = True)
async def pair(ctx):
	await ctx.send("Vous remplissez toute les conditions !")

@bot.command()
@commands.has_permissions(ban_members = True)
async def unban(ctx, user, *reason):
	reason = " ".join(reason)
	userName, userId = user.split("#")
	bannedUsers = await ctx.guild.bans()
	for i in bannedUsers:
		if i.user.name == userName and i.user.discriminator == userId:
			await ctx.guild.unban(i.user, reason = reason)
			await ctx.send(f"{user} à été unban.")
			return
	#Ici on sait que lutilisateur na pas ete trouvé
	await ctx.send(f"L'utilisateur {user} n'est pas dans la liste des bans")

@bot.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, user : discord.User, *reason):
	reason = " ".join(reason)
	await ctx.guild.kick(user, reason = reason)
	await ctx.send(f"{user} à été kick.")

@bot.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx, nombre : int):
	messages = await ctx.channel.history(limit = nombre + 1).flatten()
	for message in messages:
		await message.delete()
	
bot.run("NzA3Njc4MjI1MDA1OTM2NjUy.XsbN8g.n4ZnavWhgkEpuPzja_8i2BzvupY")
