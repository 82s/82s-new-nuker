import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import *
import random
import os
from colorama import Fore, Style

#Put your token in the quotation marks

token = "Nzk4NjEzMDgzMTkwMzI5NDA2.YDE1cA.rnmUMAtni58KpXy9opMdrWUsr2w"

#Put your prefix in the quotation marks

prefix = "¥"

intents = discord.Intents.all()
client = commands.Bot(command_prefix=prefix, self_bot=True, intents=intents)
client.remove_command("help")


@client.event
async def on_ready():
	print(Fore.GREEN + """                        
""" + Fore.RESET)
	print(Fore.GREEN + """ _____ ____

░██████╗██████╗░
██╔════╝██╔══██╗
╚█████╗░██████╦╝
░╚═══██╗██╔══██╗
██████╔╝██████╦╝
╚═════╝░╚═════╝░
""")
	print(Fore.GREEN + f"SELF BOT IS READY" + Fore.RESET)
	print(Fore.GREEN + f"Logged in as {client.user.name}" + Fore.RESET)
	print(Fore.GREEN + f"Your account ID is: {client.user.id}" + Fore.RESET)
	print(Fore.GREEN + f"Your Customizable Prefix Is: {prefix}" + Fore.RESET)


@client.command()
async def help(ctx):
	await ctx.message.delete()
	embed = discord.Embed(color=discord.Colour.from_rgb(0, 0, 0), title=" 🎸𝙎𝘽")
	embed.set_thumbnail(url=ctx.author.avatar_url)
	embed.set_image(
	    url=
	    "https://images-ext-2.discordapp.net/external/BsglnHafsp96Wrq2bZiRs_8P8ccyYJ-lJvzSl_v6gHc/%3Fwidth%3D400%26height%3D220/https/images-ext-1.discordapp.net/external/dcxQP3xcmopqJUSMzuqnZ1Ys2rFuDm5DPbVi4ab4vDw/https/images-ext-2.discordapp.net/external/qTE8sXP4ZKuh-i_iqdQevGSe51DPNFcBGly9BiJON6Y/https/media.discordapp.net/attachments/799930255737487400/799931076398809138/image0.gif"
	)
	embed.add_field(name="𝙈𝙤𝙙𝙚𝙧𝙖𝙩𝙞𝙤𝙣", value="𝐒𝐡𝐨𝐰𝐬 𝐓𝐡𝐞 𝙢𝙤𝙙𝙚𝙧𝙖𝙩𝙞𝙤𝙣 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬")
	embed.add_field(name="𝐌𝐢𝐬𝐜", value="𝙎𝙝𝙤𝙬𝙨 𝙩𝙝𝙚 𝐌𝐢𝐬𝐜 𝙘𝙤𝙢𝙢𝙖𝙣𝙙𝙨")
	embed.add_field(name="𝙉𝙪𝙠𝙚", value="𝙎𝙝𝙤𝙬𝙨 𝙩𝙝𝙚 𝙉𝙪𝙠𝙚 𝙘𝙤𝙢𝙢𝙖𝙣𝙙𝙨")
	embed.set_footer(text=f"Coded by 🎸 Tha Prefix is {prefix}")
	await ctx.send(embed=embed)


@client.command(aliases=["misc"])
async def miscellaneous(ctx):
	await ctx.message.delete()
	embed = discord.Embed(color=discord.Colour.from_rgb(0, 0, 0),
	                      title="𝐌𝐢𝐬𝐜 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬")
	embed.set_thumbnail(url=ctx.author.avatar_url)
	embed.set_image(
	    url=
	    "https://images-ext-2.discordapp.net/external/94zdt5uRDbQL-ASxteu1TLvmSLZ0t9ceQyA7PDcnal0/https/media.discordapp.net/attachments/798375103117262918/798382963938164796/image0.gif"
	)
	embed.add_field(name="𝙨𝙩𝙧𝙚𝙖𝙢 <𝙩𝙚𝙭𝙩>",
	                value="𝙎𝙚𝙩𝙨 𝙮𝙤𝙪𝙧 𝙨𝙩𝙖𝙩𝙪𝙨 𝙖𝙨 𝙨𝙩𝙧𝙚𝙖𝙢𝙞𝙣𝙜")
	embed.add_field(name="𝙜𝙖𝙢𝙚 <𝙩𝙚𝙭𝙩>", value="𝙎𝙚𝙩𝙨 𝙮𝙤𝙪𝙧 𝙨𝙩𝙖𝙩𝙪𝙨 𝙖𝙨 𝙥𝙡𝙖𝙮𝙞𝙣𝙜")
	embed.add_field(name="𝙖𝙫 <𝙪𝙨𝙚𝙧>", value="𝙎𝙚𝙣𝙙𝙨 𝙩𝙝𝙚 𝙢𝙚𝙣𝙩𝙞𝙤𝙣𝙚𝙙 𝙪𝙨𝙚𝙧𝙨 𝙖𝙫𝙖𝙩𝙖𝙧")
	embed.add_field(name="𝙡𝙚𝙖𝙫𝙚", value="𝙇𝙚𝙖𝙫𝙚𝙨 𝙩𝙝𝙚 𝙜𝙪𝙞𝙡𝙙")
	embed.add_field(name="𝙨𝙚𝙧𝙫𝙚𝙧𝙣𝙖𝙢𝙚 <𝙩𝙚𝙭𝙩>",
	                value="𝙎𝙚𝙩𝙨 𝙩𝙝𝙚 𝙨𝙚𝙧𝙫𝙚𝙧 𝙣𝙖𝙢𝙚 𝙖𝙨 𝙩𝙝𝙚 𝙩𝙚𝙭𝙩")
	embed.set_footer(text=f"Coded By 🎸 | Prefix is {prefix}")
	await ctx.send(embed=embed)


@client.command()
async def nuke(ctx):
	await ctx.message.delete()
	embed = discord.Embed(color=discord.Colour.from_rgb(0, 0, 0),
	                      title="𝐍𝐮𝐤𝐞 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬")
	embed.set_thumbnail(url=ctx.author.avatar_url)
	embed.set_image(
	    url=
	    "https://media.discordapp.net/attachments/798365432158617611/799147226974781470/image0.gif?width=513&height=513"
	)
	embed.add_field(name="𝙗𝙖𝙣𝙖𝙡𝙡", value="𝘽𝙖𝙣𝙨 𝙖𝙡𝙡 𝙩𝙝𝙚 𝙪𝙨𝙚𝙧𝙨 𝙞𝙣 𝙩𝙝𝙚 𝙜𝙪𝙞𝙡𝙙")
	embed.add_field(name="𝙠𝙞𝙘𝙠𝙖𝙡𝙡", value="𝙆𝙞𝙘𝙠𝙨 𝙖𝙡𝙡 𝙢𝙚𝙢𝙗𝙚𝙧𝙨 𝙞𝙣 𝙩𝙝𝙚 𝙜𝙪𝙞𝙡𝙙")
	embed.add_field(name="𝙨𝙥𝙖𝙢𝙘𝙝𝙖𝙣 <𝙩𝙚𝙭𝙩>",
	                value="𝙎𝙥𝙖𝙢 𝙘𝙧𝙚𝙖𝙩𝙚𝙨 𝙘𝙝𝙖𝙣𝙣𝙚𝙡𝙨 𝙬𝙞𝙩𝙝 𝙩𝙝𝙚 𝙣𝙖𝙢𝙚 𝙤𝙛 𝙩𝙝𝙚 𝙩𝙚𝙭𝙩")
	embed.add_field(name="𝙨𝙥𝙖𝙢 <𝙩𝙚𝙭𝙩>", value="𝙎𝙥𝙖𝙢𝙨 𝙩𝙝𝙚 𝙙𝙚𝙨𝙞𝙧𝙚𝙙 𝙩𝙚𝙭𝙩")
	embed.add_field(name="𝙜𝙨𝙥𝙖𝙢 <𝙩𝙚𝙭𝙩>", value="𝙂𝙝𝙤𝙨𝙩 𝙨𝙥𝙖𝙢𝙨 𝙩𝙝𝙚 𝙙𝙚𝙨𝙞𝙧𝙚𝙙 𝙩𝙚𝙭𝙩")
	embed.add_field(name="𝙙𝙢𝙖𝙡𝙡 <𝙩𝙚𝙭𝙩>",
	                value="𝙙𝙢𝙨 𝙖𝙡𝙡 𝙪𝙨𝙚𝙧𝙨 𝙞𝙣 𝙩𝙝𝙚 𝙜𝙪𝙞𝙡𝙙 𝙩𝙝𝙚 𝙩𝙚𝙭𝙩")
	embed.set_footer(text=f"Coded by 🎸 | Prefix is {prefix}")
	await ctx.send(embed=embed)


@client.command(aliases=["mod"])
async def moderation(ctx):
	await ctx.message.delete()
	embed = discord.Embed(color=discord.Colour.from_rgb(0, 0, 0),
	                      title="𝐌𝐨𝐝𝐞𝐫𝐚𝐭𝐢𝐨𝐧 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬")
	embed.set_thumbnail(url=ctx.author.avatar_url)
	embed.set_image(
	    url=
	    "https://cdn.discordapp.com/attachments/790266937808257074/800494019053617192/image1-1.gif"
	)
	embed.add_field(name="𝙗𝙖𝙣 <𝙪𝙨𝙚𝙧>", value="𝘽𝙖𝙣𝙨 𝙩𝙝𝙚 𝙢𝙚𝙣𝙩𝙞𝙤𝙣𝙚𝙙 𝙪𝙨𝙚𝙧")
	embed.add_field(name="𝙠𝙞𝙘𝙠 <𝙪𝙨𝙚𝙧>", value="𝙆𝙞𝙘𝙠𝙨 𝙩𝙝𝙚 𝙢𝙚𝙣𝙩𝙞𝙤𝙣𝙚𝙙 𝙪𝙨𝙚𝙧")
	embed.add_field(name="𝙘𝙡𝙚𝙖𝙧 <𝙖𝙢𝙤𝙪𝙣𝙩>",
	                value="𝘿𝙚𝙡𝙚𝙩𝙨𝙨 𝙩𝙝𝙚 𝙙𝙚𝙨𝙞𝙧𝙚𝙙 𝙖𝙢𝙤𝙪𝙣𝙩 𝙤𝙛 𝙢𝙚𝙨𝙨𝙖𝙜𝙚𝙨")
	embed.set_footer(text=f"Coded by 🎸 | Prefix is {prefix}")
	await ctx.send(embed=embed)


@client.event
async def on_command_error(ctx, error):
	embed = discord.Embed(color=discord.Colour.from_rgb(0, 0, 0),
	                      description=f"{error}")
	embed.set_author(name="𝙀𝙍𝙍𝙊𝙍")
	await ctx.send(embed=embed)


@client.command()
async def av(ctx, member: discord.Member):
	await ctx.message.delete()
	embed = discord.Embed(color=discord.Colour.from_rgb(0, 0, 0),
	                      title=f"{member}'𝙨 𝘼𝙫𝙖𝙩𝙖𝙧")
	embed.set_image(url=member.avatar_url)
	await ctx.send(embed=embed)


@client.command()
async def stream(ctx, *, text):
	await ctx.message.delete()
	await client.change_presence(
	    activity=discord.Streaming(name=text, url="https://www.twitch.tv/🎸"))


@client.command()
async def game(ctx, *, text):
	await ctx.message.delete()
	await client.change_presence(activity=discord.Game(name=text))


@client.command()
async def leave(ctx):
	await ctx.message.delete()
	await ctx.send("Cya Retards")
	await ctx.guild.leave()


@client.command()
async def servername(ctx, *, text):
	await ctx.message.delete()
	await ctx.guild.edit(name=text)


@client.command(aliases=["ball"])
async def banall(ctx):
	await ctx.message.delete()
	guild = ctx.guild
	for member in guild.members:
		try:
			await member.ban()
			print(f"{member} has been banned")
		except:
			print(f"{member} has not been banned")
		continue


@client.command(aliases=["kall"])
async def kickall(ctx):
	await ctx.message.delete()
	guild = ctx.guild
	for member in guild.members:
		try:
			await member.kick()
			print(f"{member} has been kicked")
		except:
			print(f"{member} has not been kicked")
		continue


@client.command(aliases=["massdm"])
async def dmall(ctx, *, text):
	await ctx.message.delete()
	guild = ctx.guild
	for member in guild.members:
		try:
			await member.send(text)
			print(f"Message sent to {member}")
		except:
			print(f"Message not sent to {member}")
		continue


@client.command()
async def spam(ctx, *, text):
	await ctx.message.delete()
	amount = 100
	for i in range(amount):
		await ctx.send(text)


@client.command()
async def gspam(ctx, *, text):
	await ctx.message.delete()
	amount = 100
	for i in range(amount):
		msg = await ctx.send(text)
		await msg.delete()


@client.command()
async def spamchan(ctx, *, text):
	await ctx.message.delete()
	amount = 100
	for i in range(amount):
		await ctx.guild.create_text_channel(name=text)


@client.command()
async def ban(ctx, member: discord.Member):
	await ctx.message.delete()
	await member.ban()
	embed = discord.Embed(color=discord.Colour.from_rgb(0, 0, 0),
	                      title="𝙈𝙚𝙢𝙗𝙚𝙧 𝘽𝙖𝙣𝙣𝙚𝙙",
	                      description=f"{member} 𝙃𝙖𝙨 𝘽𝙚𝙚𝙣 𝘽𝙖𝙣𝙣𝙚𝙙")
	embed.set_footer(text=f"🎸 𝙍𝙪𝙣𝙨 {member}")


@client.command()
async def kick(ctx, member: discord.Member):
	await ctx.message.delete()
	await member.kick()
	embed = discord.Embed(color=discord.Colour.from_rgb(0, 0, 0),
	                      title="𝙈𝙚𝙢𝙗𝙚𝙧 𝙆𝙞𝙘𝙠𝙚𝙙",
	                      description=f"{member} 𝙃𝙖𝙨 𝘽𝙚𝙚𝙣 𝙆𝙞𝙘𝙠𝙚𝙙")
	embed.set_footer(text=f"🎸 𝙍𝙪𝙣𝙨 {member}")


@client.command()
async def clear(ctx, amount=1):
	await ctx.message.delete()
	await ctx.channel.purge(limit=amount)


client.run(token, bot=False)
