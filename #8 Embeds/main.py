import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix = "!", description = "Bot de Titouan")
funFact = ["L'eau mouille", 
			"Le feu brule", 
			"Lorsque vous volez, vous ne touchez pas le sol", 
			"Winter is coming", "Mon créateur est Titouan", 
			"Il n'est pas possible d'aller dans l'espace en restant sur terre", 
			"La terre est ronde",
			"La moitié de 2 est 1",
			"7 est un nombre heureux",
			"Les allemands viennent d'allemagne",
			"Le coronavirus est un virus se répandant en Europe, en avez vous entendu parler ?",
			"J'apparais 2 fois dans l'année, a la fin du matin et au début de la nuit, qui suis-je ?",
			"Le plus grand complot de l'humanité est",
			"Pourquoi lisez vous ca ?"]

@bot.event
async def on_ready():
	print("Ready !")

@bot.command()
async def ban(ctx, user : discord.User, *, reason = "Aucune raison n'a été donné"):
	#await ctx.guild.ban(user, reason = reason)
	embed = discord.Embed(title = "**Banissement**", description = "Un modérateur a frappé !", url = "https://www.youtube.com/channel/UChDVo_Uqomuk7KnMVp-Lhhw?view_as=subscriber", color=0xfa8072)
	embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url, url = "https://www.youtube.com/channel/UChDVo_Uqomuk7KnMVp-Lhhw?view_as=subscriber")
	embed.set_thumbnail(url = "https://discordemoji.com/assets/emoji/BanneHammer.png")
	embed.add_field(name = "Membre banni", value = user.name, inline = True)
	embed.add_field(name = "Raison", value = reason, inline = True)
	embed.add_field(name = "Modérateur", value = ctx.author.name, inline = True)
	embed.set_footer(text = random.choice(funFact))

	await ctx.send(embed = embed)

bot.run("NzA3Njc4MjI1MDA1OTM2NjUy.XsuSwA._2rtd7BaWtOrUtKoQOv5i7TuqEg")

































"""
https://www.youtube.com/channel/UChDVo_Uqomuk7KnMVp-Lhhw?view_as=subscriber
"""


"""
https://discordemoji.com/assets/emoji/BanneHammer.png
"""


"""
funFact = ["L'eau mouille", 
			"Le feu brule", 
			"Lorsque vous volez, vous ne touchez pas le sol", 
			"Winter is coming", "Mon créateur est Titouan", 
			"Il n'est pas possible d'aller dans l'espace en restant sur terre", 
			"La terre est ronde",
			"La moitié de 2 est 1",
			"7 est un nombre heureux",
			"Les allemands viennent d'allemagne",
			"Le coronavirus est un virus se répandant en Europe, en avez vous entendu parler ?",
			"J'apparais 2 fois dans l'année, a la fin du matin et au début de la nuit, qui suis-je ?",
			"Le plus grand complot de l'humanité est",
			"Pourquoi lisez vous ca ?"]
"""