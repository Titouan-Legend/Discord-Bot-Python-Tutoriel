import discord
from discord.ext import commands
import cog_2
import random

bot = commands.Bot(command_prefix="!", description="Bot de Titouan !")


@bot.event
async def on_ready():
    print("Ready !")


@bot.command()
async def hello(ctx):
    await ctx.send("Hello ! ")


@bot.command()
async def load(ctx, name=None):
    if name:
        bot.load_extension(name)


@bot.command()
async def unload(ctx, name=None):
    if name:
        bot.unload_extension(name)


@bot.command()
async def reload(ctx, name=None):
    if name:
        try:
            bot.reload_extension(name)
        except:
            bot.load_extension(name)

@bot.command()
async def test(ctx):
    channel = bot.get_channel(23)
    channel.send("hey")

bot.add_cog(cog_2.CogOwner(bot))
bot.run("NzA3Njc4MjI1MDA1OTM2NjUy.Xvm5bw.U2WFzT3YfRIhSe8sTy1VqjjCleY")
