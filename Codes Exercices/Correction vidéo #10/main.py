import discord
from discord.ext import commands, tasks
import random

bot = commands.Bot(command_prefix = "!", description = "Bot de Titouan")

@bot.event
async def on_ready():
	print("Ready !")

@bot.command()
async def role(ctx, *,nom):
    roleMembre = ""
    roles = ctx.guild.roles
    for role in roles:
        if role.name == nom:
            roleMembre = role
    if roleMembre == "":
        roleMembre = await ctx.guild.create_role(name = nom, reason = "Un membre a fait la commande role.")
    await ctx.message.author.add_roles(roleMembre, reason = "commande")

bot.run("NzA3Njc4MjI1MDA1OTM2NjUy.XttpOQ.OE8mo1cqE0O6MHFDy3fPniV69Xk")