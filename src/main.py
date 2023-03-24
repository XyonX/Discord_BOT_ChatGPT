import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print('bot logged in as : {0.user}'.format(bot))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswitch('$hello'):
        await message.channel.send('hello')

load_dotenv()

api_key = os.environ.get('Discord_Api')
bot.run(api_key)




