import discord
from discord.ext import commands, tasks
from discord.utils import get
import datetime
from Data.database_handler import DatabaseHandler

intents = discord.Intents().default()
intents.members = True

bot = commands.Bot(command_prefix = "!", description = "Bot de Titouan", intents=intents)
database_handler = DatabaseHandler("database.db")

@bot.event
async def on_ready():
	check_for_unmute.start()
	print("Ready !")

async def get_muted_role(guild : discord.Guild) -> discord.Role:
	role = get(guild.roles, name="Muted")
	if role is not None:
		return role
	else:
		permissions = discord.Permissions(send_messages=False)
		role = await guild.create_role(name="Muted", permissions=permissions)
		return role

@bot.command()
async def mute(ctx, member : discord.Member, seconds : int):
	muted_role = await get_muted_role(ctx.guild)
	database_handler.add_tempmute(member.id, ctx.guild.id, datetime.datetime.utcnow() + datetime.timedelta(seconds=seconds))
	await member.add_roles(muted_role)
	await ctx.send(f"{member.mention} a été muté ! 🎙")

@tasks.loop(minutes=1)
async def check_for_unmute():
	for guild in bot.guilds:
		active_tempmute = database_handler.active_tempmute_to_revoke(guild.id)
		if len(active_tempmute) > 0:
			muted_role = await get_muted_role(guild)
			for row in active_tempmute:
				member = guild.get_member(row["user_id"])
				database_handler.revoke_tempmute(row["id"])
				await member.remove_roles(muted_role)

bot.run("ODcxNDU1MzkwODAwNDI0OTkw.YQbkFA.c06CL-KCOyCSPawb7Ilbo8sf5nk")