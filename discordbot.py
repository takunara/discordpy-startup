from discord.ext import commands
import os
import traceback
import time
from time import sleep
import threading

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


#追加--------------------------
@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
#async def on_ready():
#    while True:
#        if time.strftime('%H:%M',time.localtime())=='22:26':
#            channel = client.get_channel('20分模写')
#            await client.send_message(channel, '勝手に喋るよ')
#            sleep(60)
#------------------------------    

#@bot.event
#async def on_command_error(ctx, error):
#    await ctx.send(str(error))
#@bot.command()
#async def ping(ctx):
#    await ctx.send('pong')


bot.run(token)
