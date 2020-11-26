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
    await message.channel.send(f"> {message.content}\n{message.author}")
    await bot.process_commands(message)

@bot.event
async def on_message_delete(message):
    await message.channel.send(f"Le message de {message.author} a été supprimé \n> {message.content}")

@bot.event
async def on_message_edit(before, after):
    await before.channel.send(f"{before.author} a édité son message :\nAvant -> {before.content}\nAprès -> {after.content}")

@bot.event
async def on_member_join(member):
    channel = member.guild.get_channel(714786510238384532)
    await channel.send(f"Acceuillons a bras ouvert {member.mention} ! Bienvenue dans ce magnifique serveur :)")

@bot.event
async def on_member_remove(member):
    channel = member.guild.get_channel(714786510238384532)
    await channel.send(f"En cette belle journée nous déplorons la perte d'un membre bien aimé, {member.mention}.")

@bot.event
async def on_reaction_add(reaction, user):
    await reaction.message.add_reaction(reaction.emoji)

@bot.event
async def on_typing(channel, user, when):
    await channel.send(f"{user.name} a commencé à écrire dans ce channel le {when}.")

@bot.command()
async def coucou(ctx):
    await ctx.send("Coucou !")


bot.run("NzA3Njc4MjI1MDA1OTM2NjUy.XsuSwA._2rtd7BaWtOrUtKoQOv5i7TuqEg")
