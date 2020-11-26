import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!", description = "Bot de Titouan")

@bot.event
async def on_ready():
	print("Ready !")

@bot.command()
async def say(ctx, number, *texte):
	for i in range(int(number)):
		await ctx.send(" ".join(texte))

@bot.command()
async def getInfo(ctx, info):
	server = ctx.guild
	if info == "memberCount":
		await ctx.send(server.member_count)
	elif info == "numberOfChannel":
		await ctx.send(len(server.voice_channels) + len(server.text_channels))
	elif info == "name":
		await ctx.send(server.name)
	else:
		await ctx.send("Etrange... Je ne connais pas cela")

bot.run("NzA3Njc4MjI1MDA1OTM2NjUy.XrbSHw.hy9e6ZxYN4W_ccbg6GpXIlzgK0w")