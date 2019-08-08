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
    await ctx.send('pong')

# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    channel = client.get_channel("20分模写")
    await channel.send('時間だよ')  

#ループ処理実行
loop.start()

bot.run(token)
