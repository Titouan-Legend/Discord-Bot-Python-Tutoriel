import discord
from discord.ext import commands
from discord_slash import ButtonStyle, SlashCommand
from discord_slash.utils.manage_components import *

bot = commands.Bot(command_prefix = "!", description = "Bot de Titouan")
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
    print("Ready !")


@bot.command()
async def choix(ctx):
    buttons = [
        create_button(
            style=ButtonStyle.blue,
            label="Choisissez moi",
            custom_id="oui"
        ),
        create_button(
            style=ButtonStyle.danger,
            label="SURTOUT PAS MOI!!!",
            custom_id="non"
        )
    ]
    action_row = create_actionrow(*buttons)
    fait_choix = await ctx.send("Faites votre choix !", components=[action_row])

    def check(m):
        return m.author_id == ctx.author.id and m.origin_message.id == fait_choix.id

    button_ctx = await wait_for_component(bot, components=action_row, check=check)
    if button_ctx.custom_id == "oui":
        await button_ctx.edit_origin(content="Bravo !")
    else:
        await button_ctx.edit_origin(content="...")

@bot.command()
async def quiz(ctx):
    select = create_select(
        options=[
            create_select_option("Haha tRoP mArRaNt lOl", value="1", emoji="😂"),
            create_select_option("...", value="2", emoji="😏"),
            create_select_option("friendzone", value="3", emoji="💛"),
            create_select_option("renard", value="4", emoji="🦊")
        ],
        placeholder="Choisis un emoji...",
        min_values=1,
        max_values=1
    )
    fait_choix = await ctx.send("Quel est le meilleur emoji de tout les temps ?", components=[create_actionrow(select)])

    def check(m):
        return m.author_id == ctx.author.id and m.origin_message.id == fait_choix.id

    choice_ctx = await wait_for_component(bot, components=select, check=check)

    if choice_ctx.values[0] == "4":
        await choice_ctx.send("Bonne réponse ! 🦊")
    else:
        await choice_ctx.send("Mauvaise réponse... 😒")



bot.run("ODcxNDU1MzkwODAwNDI0OTkw.YQbkFA.HwW7Texa9j8TWgKBKrO4cU-U4Yg")















































