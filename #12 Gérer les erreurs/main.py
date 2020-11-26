import discord
from discord.ext import commands
import youtube_dl
import asyncio

bot = commands.Bot(command_prefix="!", description="Bot de Titouan !")


@bot.event
async def on_ready():
    print("Ready !")


@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		await ctx.send("Mmmmmmh, j'ai bien l'impression que cette commande n'existe pas :/")

	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send("Il manque un argument.")
	elif isinstance(error, commands.MissingPermissions):
		await ctx.send("Vous n'avez pas les permissions pour faire cette commande.")
	elif isinstance(error, commands.CheckFailure):
		await ctx.send("Oups vous ne pouvez iutilisez cette commande.")
	if isinstance(error.original, discord.Forbidden):
		await ctx.send("Oups, je n'ai pas les permissions nécéssaires pour faire cette commmande")


def good_channel(ctx):
	return ctx.message.channel.id == 724977575696400435

@bot.command()
async def coucou(ctx, nombre : int):
	for i in range(nombre):
		await ctx.send("coucou")

@coucou.error
async def coucou_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send("La commande coucou prend en parametre un nombre.")
		await ctx.send("Veuillez réessayer.")

@bot.command()
@commands.has_permissions(manage_messages=True)
@commands.check(good_channel)
async def clear(ctx, nombre: int):
    messages = await ctx.channel.history(limit=nombre + 1).flatten()
    for message in messages:
        await message.delete()


bot.run("NzA3Njc4MjI1MDA1OTM2NjUy.Xu9qow.f96I9aur_mowpZCJ7ortxfdS79I")
