from discord.ext import commands
import os
import traceback
import time
from time import sleep
import threading

bot = discord.Client() # 接続に使用するオブジェクト
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_ready():
    while True:
        channel = client.get_channel('20分模写')
        await bot.send_message(channel, 'おはよう')
        time.sleep(10)

bot.run(token)
