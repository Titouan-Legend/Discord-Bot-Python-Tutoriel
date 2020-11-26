import discord
from discord.ext import commands
import random
import time

bot = commands.Bot(command_prefix = "!", description = "Bot de Titouan")

@bot.event
async def on_ready():
	print("Ready !")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if isinstance(message.channel, discord.DMChannel): #Check if message in DM
        guild = bot.get_guild(707283961121996922)
        channel = guild.get_channel(715127235564273764)
        await channel.send(message.author.mention + message.content)
        return


bot.run("NzA3Njc4MjI1MDA1OTM2NjUy.XsuSwA._2rtd7BaWtOrUtKoQOv5i7TuqEg")
