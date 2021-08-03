import discord
import random
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option, create_choice, create_permission
from discord_slash.model import SlashCommandPermissionType

bot = commands.Bot(command_prefix="!", description = "Bot tuto")
slash = SlashCommand(bot, sync_commands = True)

@bot.event
async def on_ready():
	print("Ready !")

@slash.slash(name="lancer", guild_ids=[871456214016458772], description="Lance un dé pour toi", options=[
	create_option(
		name="tricher", 
		description="Tricher pour sortir toujours le même nombre (4)", 
		option_type=3,
		required=True,
		choices=[
			create_choice(
				name="Oui",
				value="y"
			),
			create_choice(
				name="Non",
				value="n"
			)
		]
	),
	create_option(name="limite_inferieure", description="Le nombre le plus bas que le dé peux donner.", option_type=4, required=False),
	create_option(name="limite_superieure", description="Le nombre le plus haut que le dé peux donner.", option_type=4, required=False)
])
async def lancer(ctx, tricher, limite_inferieure = 1, limite_superieure = 6):
	await ctx.send("Je lance le dé...")
	num = random.randint(limite_inferieure, limite_superieure)
	if tricher == "y":
		num = 4
	await ctx.send(f"**{num}** 🎲!")

@slash.slash(name="bonjour", guild_ids=[871456214016458772], description="Cette commande dis bonjour !")
@slash.permission(
	guild_id=871456214016458772,
	permissions=[
		create_permission(871456214016458772, SlashCommandPermissionType.ROLE, False),
		create_permission(871463050409050112, SlashCommandPermissionType.ROLE, True),
	]
)
async def bonjour(ctx):
	await ctx.send(ctx.author.display_name + " dis bonjour !")






















bot.run("ODcxNDU1MzkwODAwNDI0OTkw.YQbkFA.tf3b3iiA9uCYen5GNjlCGMia55M")