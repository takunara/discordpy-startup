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
import asyncio


token = os.environ['DISCORD_BOT_TOKEN']


client = discord.Client()

@client.event
async def on_ready():
    asyncio.ensure_future(greeting_gm())

async def greeting_gm():
    await message.channel.send("text")
    await asyncio.sleep(10)

client.run(token)
