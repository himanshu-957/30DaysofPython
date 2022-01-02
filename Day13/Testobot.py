import nextcord
from nextcord.ext import commands
clients = commands.Bot(command_prefix="!")

@clients.command()
async def ping(ctx):
    await ctx.reply("Pong!!")
from flask import Flask, jsonify
app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)