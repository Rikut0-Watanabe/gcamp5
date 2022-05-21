import discord
from discord.ext import commands
from getsearchresult import *

TOKEN = ""
bot = commands.Bot(command_prefix="!")
bot.remove_command("help")

@bot.event
async def on_ready():
    print("起動完了")

@bot.command()
async def test(ctx):
    await ctx.send("test.ok!")

async def search(ctx, query):
    result = get_search_result(query)
    result_items_list = summarize_search_results(result)
    for i in range(0, 3):
        await ctx.send(str(i) + ". " + str(result_items_list[i].title) + "\n" + str(result_items_list[i].url))


bot.run(TOKEN)
