import nextcord
from nextcord.ext import commands
import botoken2
import random
import os
import aiohttp

def main():
    clients = commands.Bot(command_prefix="!")
    clients.remove_command("help")
    
    @clients.command()
    async def help(ctx):
        embed = nextcord.Embed(title='Help', description='!ping command for checking(It will send Pong)\n !hello command for asking bots name\n !fine as a reply for how are you\n !same for a smile')
        await ctx.send(embed=embed)
        
    for folder in os.listdir("modules"):
        if os.path.exists(os.path.join("modules", folder, "cog.py")):
            clients.load_extension(f"modules.{folder}.cog")
            
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
#async def on_message(ctx):
#     if ctx.content.startswith("Hello"):
#         channel = ctx.channel
#         channel.send("Hi")
    clients.run(botoken2.TOKEN)

if __name__ == '__main__':
    main()