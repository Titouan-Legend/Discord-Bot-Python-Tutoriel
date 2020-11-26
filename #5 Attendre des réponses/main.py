import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!", description = "Bot de Titouan")

@bot.event
async def on_ready():
	print("Ready !")

@bot.command()
async def cuisiner(ctx):
	await ctx.send("Envoyez le plat que vous voulez cuisiner")

	def checkMessage(message):
		return message.author == ctx.message.author and ctx.message.channel == message.channel

	try:
		recette = await bot.wait_for("message", timeout = 10, check = checkMessage)
	except:
		await ctx.send("Veuillez réitérer la commande.")
		return
	message = await ctx.send(f"La préparation de {recette.content} va commencer. Veuillez valider en réagissant avec ✅. Sinon réagissez avec ❌")
	await message.add_reaction("✅")
	await message.add_reaction("❌")


	def checkEmoji(reaction, user):
		return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "❌")

	try:
		reaction, user = await bot.wait_for("reaction_add", timeout = 10, check = checkEmoji)
		if reaction.emoji == "✅":
			await ctx.send("La recette a démarré.")
		else:
			await ctx.send("La recette a bien été annulé.")
	except:
		await ctx.send("La recette a bien été annulé.")



bot.run("NzA3Njc4MjI1MDA1OTM2NjUy.Xr6t8A.nZ_INNn_Xl-BuRcZ-qRGwiPqVXU")

"""
!cuisiner -> titouan
frites : coucou
titouan : pates

"""



"""

✅❌
"""