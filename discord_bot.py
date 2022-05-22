from http import client
import discord
from discord.ext import commands
from testsearch import *
import random

TOKEN = ""

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)
bot.remove_command("help")

@bot.event
async def on_ready():
    print("起動完了")

@bot.command()
async def test(ctx):
    await ctx.send("test.ok!")

@bot.command()
async def setup(ctx, guild_id):
    
    await ctx.send("セットアップ完了です！")

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

    
@bot.command()
async def t(ctx, pnum, guild_name, channel1_name, channel2_name):
    state = ctx.author.voice
    if state is None:
        await ctx.send("チーム振り分け用のボイスチャンネルに入室して下さい")

    else:
        guild = discord.utils.get(bot.guilds, name=guild_name)
        channel1 = discord.utils.get(guild.voice_channels, name=channel1_name)
        channel2 = discord.utils.get(guild.voice_channels, name=channel2_name)
        channel = [channel1, channel2]
        channel_mem = [user for user in state.channel.members]
        random.shuffle(channel_mem)
        for i in range(0, int(pnum)):
            chan_num = i % int(2)
            await channel_mem[i].move_to(channel[chan_num])
        await ctx.send("振り分け完了")


bot.run(TOKEN)