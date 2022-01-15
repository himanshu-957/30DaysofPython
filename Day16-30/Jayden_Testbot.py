import nextcord
from nextcord.ext import commands
import botoken
import random
import aiohttp
clients = commands.Bot(command_prefix="!")

@clients.command()
async def ping(ctx):
    await ctx.send("Pong!!")

@clients.command()
async def hello(ctx):
    await ctx.send("Hey! I am {0.user}".format(clients))
    await ctx.send("How are you?")


@clients.command()
async def fine(ctx):
    await ctx.send("That's Great")
    await ctx.send("Nice to meet you")

@clients.command()
async def same(ctx):
    await ctx.send(":)")

@clients.command(pass_context=True)
async def meme(ctx):
    embed = nextcord.Embed(title="", description="")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)
#@clients.event
#async def on_message(message):
#    if message.content.startswith("Fine"):
#        channel = message.channel
#        channel.send("That's great")
clients.run(botoken.TOKEN)