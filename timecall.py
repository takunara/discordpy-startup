#coding:UTF-8
import discord
from discord.ext import tasks
from datetime import datetime 

TOKEN = NjA4OTg4NTI3NTUxNTc4MTEz.XUw01A.IEZDiSirvDs186lL_CiUnF58r0s #トークン
CHANNEL_ID = "20分模写" #チャンネルID
# 接続に必要なオブジェクトを生成
client = discord.Client()

# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    if now == '07:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('おはよう')  

#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
