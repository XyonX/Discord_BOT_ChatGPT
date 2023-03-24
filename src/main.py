import discord
import os
from dotenv import load_dotenv

intent = discord.Intents.default()
client = discord.Client(intents=intent)


@client.event
async def on_ready():
    print('bot logged in as : {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswitch('$hello'):
        await message.channel.send('hello')

load_dotenv()

api_key = os.environ.get('Discord_Api')
client.run(api_key)




