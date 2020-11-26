import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!", description = "Bot de Titouan")

@bot.event
async def on_ready():
	print("Ready !")

@bot.command()
async def say(ctx, *texte):
	await ctx.send(" ".join(texte))

@bot.command()
async def chinese(ctx, *text):
	chineseChar = "丹书匚刀巳下呂廾工丿片乚爪冂口尸Q尺丂丁凵V山乂Y乙"
	chineseText = []
	for word in text:
		for char in word:
			if char.isalpha():
				index = ord(char) - ord("a")
				transformed = chineseChar[index]
				chineseText.append(transformed)
			else:
				chineseText.append(char)
		chineseText.append(" ")
	await ctx.send("".join(chineseText))


bot.run("NzA3Njc4MjI1MDA1OTM2NjUy.XrbSHw.hy9e6ZxYN4W_ccbg6GpXIlzgK0w")