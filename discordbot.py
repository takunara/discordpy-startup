from discord.ext import commands
import os
import traceback
import time
from time import sleep
import threading

#bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


#追加--------------------------
bot = discord.Client() # 接続に使用するオブジェクト

@bot.event

async def on_ready():
    while True:
        channel = client.get_channel('20分模写')
        await bot.send_message(channel, 'おはよう')
        time.sleep(10)

client.run(token)


"""
async def on_ready():
    while True:
        if time.strftime('%H:%M',time.localtime())=='22:33':
            channel = client.get_channel('20分模写')
            await client.send_message(channel, '勝手に喋るよ')
            sleep(10)
            
"""            
#------------------------------    
    
#@bot.event
#async def on_command_error(ctx, error):
#    await ctx.send(str(error))
#@bot.command()
#async def ping(ctx):
#    await ctx.send('pong')


bot.run(token)
