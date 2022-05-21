import discord
from discord.ext import commands
from getsearchresult import *

TOKEN = "OTc3NDQ4NjA2NzIwMjA4OTc2.GOCC__.GkJ4o2whOx80uURQJG9j7Hs2i8Z9U9uyWKb6wA"
bot = commands.Bot(command_prefix="!")
bot.remove_command("help")

@bot.event
async def on_ready():
    print("起動完了")

@bot.command()
async def test(ctx):
    await ctx.send("test.ok!")

@bot.command()
async def s(ctx, query):
    result = get_search_results(query)
    result_items_list = summarize_search_results(result)
    for i in range(0, 3):
        await ctx.send(str(i) + ". " + str(result_items_list[i].title) + "\n" + str(result_items_list[i].url))


bot.run(TOKEN)
