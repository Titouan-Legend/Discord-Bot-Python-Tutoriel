import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!", description = "Bot de Titouan")

@bot.event
async def on_ready():
	print("Ready !")

@bot.command()
async def coucou(ctx):
	await ctx.send("Coucou !")

@bot.command()
async def serverInfo(ctx):
	server = ctx.guild
	numberOfTextChannels = len(server.text_channels)
	numberOfVoiceChannels = len(server.voice_channels)
	serverDescription = server.description
	numberOfPerson = server.member_count
	serverName = server.name
	message = f"Le serveur **{serverName}** contient *{numberOfPerson}* personnes ! \nLa description du serveur est {serverDescription}. \nCe serveur possède {numberOfTextChannels} salons écrit et {numberOfVoiceChannels} salon vocaux."
	await ctx.send(message)

bot.run("NzA3Njc4MjI1MDA1OTM2NjUy.XrPuIw.IM2AN79o-PKcdQi_s_jFUM4Br8M") #Ceci est le token de mon bot. Changez le avec celui de votre bot