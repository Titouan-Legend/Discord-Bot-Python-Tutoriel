import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!", description = "Bot de Titouan")

@bot.event
async def on_ready():
	print("Ready !")

@bot.command()
async def bonjour(ctx):
	serverName = ctx.guild.server.name
	await ctx.send(f"Bonjour jeune *padawan* ! Savais tu que tu te trouvais dans le serveur *{serverName}*, c'est d'ailleurs un super serveur puisque **JE** suis dedans.")

bot.run("NzA3Njc4MjI1MDA1OTM2NjUy.XrPuIw.IM2AN79o-PKcdQi_s_jFUM4Br8M")