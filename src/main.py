import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print('bot logged in as : {0.user}'.format(bot))


@bot.event
async def on_message(message):
    print("Received message: ", message.content)
    if message.author == bot.user:
        return
    if message.content.startswith('!hello'):
        print("Sending response...")
        await message.channel.send('hello')


load_dotenv()

api_key = os.environ.get('Discord_Api')
bot.run(api_key)




