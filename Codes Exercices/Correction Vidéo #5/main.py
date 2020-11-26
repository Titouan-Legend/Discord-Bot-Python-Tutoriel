import discord
from discord.ext import commands
import asyncio
import random

bot = commands.Bot(command_prefix = "!", description = "Bot de Titouan")

@bot.event
async def on_ready():
	print("Ready !")

@bot.command()
async def roulette(ctx):
	await ctx.send("La roulette commencera dans 10 secondes. Envoyez \"moi\" dans ce channel pour y participer.")
	
	players = []
	def check(message):
		return message.channel == ctx.message.channel and message.author not in players and message.content == "moi"

	try:
		while True:
			participation = await bot.wait_for('message', timeout = 10, check = check)
			players.append(participation.author)
			print("Nouveau participant : ")
			print(participation)
			await ctx.send(f"**{participation.author.name}** participe au tirage ! Le tirage commence dans 10 secondes")
	except: #Timeout
		print("Demarrage du tirrage")

	gagner = ["ban", "kick", "role personnel", "mute", "gage"]

	await ctx.send("Le tirage va commencer dans 3...")
	await asyncio.sleep(1)
	await ctx.send("2")
	await asyncio.sleep(1)
	await ctx.send("1")
	await asyncio.sleep(1)
	loser = random.choice(players)
	price = random.choice(gagner)
	await ctx.send(f"La personne qui a gagnée un {price} est...")
	await asyncio.sleep(1)
	await ctx.send("**" + loser.name + "**" + " !")




bot.run("NzA3Njc4MjI1MDA1OTM2NjUy.Xr6t8A.nZ_INNn_Xl-BuRcZ-qRGwiPqVXU")

"""
!cuisiner -> titouan
frites : coucou
titouan : pates

"""



"""

✅❌
"""