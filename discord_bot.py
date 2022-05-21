import discord
from discord.ext import commands
from testsearch import *
import random

TOKEN = "ODkzMTYwMzI0MzgxOTY2Mzg3.GDSXSN.BEVPFsExl_X1Fu-oc5mqP7CvVGoGFNhnOuivA8"
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
    await ctx.send("\"" + query + "\"" + "の検索結果を表示します：")
    result = get_search_results(query)
    result_items_list = summarize_search_results(result)
    for i in range(0, 3):
        await ctx.send(str(i+1) + ". " + str(result_items_list[i].title) + "\n" + str(result_items_list[i].url))

@bot.command()
async def d(ctx, dnum, dface):
    await ctx.send("ダイス結果を表示します：")
    for i in range(0, int(dnum)):
        result_dice = random.randint(1, int(dface))
        await ctx.send(">" + str(result_dice))

bot.run(TOKEN)