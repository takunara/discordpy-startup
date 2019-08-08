
from discord.ext import commands
import os
import traceback

import discord # インストールした discord.py
import time
from time import sleep
import threading

client = discord.Client() # 接続に使用するオブジェクト




#bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID = 608981862735675423

#@bot.event
#async def on_command_error(ctx, error):
#    await ctx.send(str(error))


#@bot.command()
#async def ping(ctx):
#    await ctx.send('pong')

@client.event
async def on_ready():
    while True:
        if time.strftime('%H:%M:%S',time.localtime())=='21:00:00':
            channel = client.get_channel(CHANNEL_ID)
            await client.send_message(channel, '勝手に喋るよ')
            sleep(5)

bot.run(token)
