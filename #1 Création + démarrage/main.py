import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!", description = "Bot de Titouan")

@bot.event
async def on_ready():
	print("Ready !")

bot.run("NzA3Njc4MjI1MDA1OTM2NjUy.XraX4A.G2e7l9ZuZTePPZ8PsV59E-rAjVo")