import nextcord
from nextcord.ext import commands
import botoken
clients = commands.Bot(command_prefix="!")

@clients.command()
async def ping(ctx):
    await ctx.reply("Pong!!")

@clients.command()
async def hello(ctx):
    await ctx.reply("Hey! I am {0.user}".format(clients))
    await ctx.reply("How are you?")


@clients.command()
async def fine(ctx):
    await ctx.reply("That's Great")
    await ctx.reply("Nice to meet you")

@clients.command()
async def same(ctx):
    await ctx.reply(":)")

#@clients.event
#async def on_message(message):
#    if message.content.startswith("Fine"):
#        channel = message.channel
#        channel.send("That's great")
clients.run(botoken.TOKEN)