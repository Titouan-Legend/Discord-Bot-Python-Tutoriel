import discord
from discord.ext import commands, tasks
import random

bot = commands.Bot(command_prefix = "!", description = "Bot de Titouan")
status = ["!help",
		"A votre service",
		"L'eau mouille", 
		"Le feu brule", 
		"Lorsque vous volez, vous ne touchez pas le sol", 
		"Winter is coming", 
		"Mon créateur est Titouan", 
		"Il n'est pas possible d'aller dans l'espace en restant sur terre", 
		"La terre est ronde",
		"La moitié de 2 est 1",
		"7 est un nombre heureux",
		"Les allemands viennent d'allemagne",
		"Le coronavirus est un virus se répandant en Europe, en avez vous entendu parler ?",
		"J'apparais 2 fois dans l'année, a la fin du matin et au début de la nuit, qui suis-je ?",
		"Le plus grand complot de l'humanité est",
		"Pourquoi lisez vous ca ?"]

@bot.event
async def on_ready():
	print("Ready !")
	changeStatus.start()

@bot.command()
async def start(ctx, secondes = 5):
	changeStatus.change_interval(seconds = secondes)

@tasks.loop(seconds = 5)
async def changeStatus():
	game = discord.Game(random.choice(status))
	await bot.change_presence(status = discord.Status.dnd, activity = game)

bot.run("NzA3Njc4MjI1MDA1OTM2NjUy.Xs-YlQ.YdYCZ384dsC7anjGvqRigN_t5O4")

































"""
status = ["!help",
		"A votre service",
		"L'eau mouille", 
		"Le feu brule", 
		"Lorsque vous volez, vous ne touchez pas le sol", 
		"Winter is coming", 
		"Mon créateur est Titouan", 
		"Il n'est pas possible d'aller dans l'espace en restant sur terre", 
		"La terre est ronde",
		"La moitié de 2 est 1",
		"7 est un nombre heureux",
		"Les allemands viennent d'allemagne",
		"Le coronavirus est un virus se répandant en Europe, en avez vous entendu parler ?",
		"J'apparais 2 fois dans l'année, a la fin du matin et au début de la nuit, qui suis-je ?",
		"Le plus grand complot de l'humanité est",
		"Pourquoi lisez vous ca ?"]
"""