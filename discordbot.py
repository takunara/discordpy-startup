"""
from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def ping(ctx):
    await ctx.send('pong--')


bot.run(token)
"""

import os
import discord
from discord.ext import tasks

TOKEN = 'NjA4OTg4NTI3NTUxNTc4MTEz.XUydOg.a7CtQoSEyRXsMTlwV0hlRl4AAJk'
CHANNEL_ID = 608981862735675423
client = discord.Client()

# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('時間だよ')  

#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
