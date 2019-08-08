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
#    await ctx.send('pong--')
    channel_bot_test = [channel for channel in client.get_all_channels() if channel.name == '20分模写'][0]
    await ctx.send_message(channel_bot_test, '勝手に喋るよ')


bot.run(token)
