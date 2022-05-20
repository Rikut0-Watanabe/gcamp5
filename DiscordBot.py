import discord
from discord.ext import commands
import time
import pygame

bot = commands.Bot(command_prefix="!")
bot.remove_command("help")

@bot.event
async def on_ready():
    print("起動完了")

@bot.command()
async def test(ctx):
    await ctx.send("test.ok!")




bot.run("ODkzMTYwMzI0MzgxOTY2Mzg3.YVXaXw.VHlTs0u3ghDsY4zYOK1SwDbwQAs")