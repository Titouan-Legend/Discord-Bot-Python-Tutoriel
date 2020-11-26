import discord
from discord.ext import commands, tasks
import random

bot = commands.Bot(command_prefix = "!", description = "Bot de Titouan")
count = 0

@bot.event
async def on_ready():
	print("Ready !")
	compter.start()

@tasks.loop(seconds = 10)
async def compter():
	global count
	channel = bot.get_channel(718434258149965835)
	await channel.send(count)
	print("count")
	count += 1

bot.run("NzA3Njc4MjI1MDA1OTM2NjUy.Xs-YlQ.YdYCZ384dsC7anjGvqRigN_t5O4")