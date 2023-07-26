import discord
import os
import openai
import requests
from dotenv import load_dotenv
from discord.ext import commands
from gpt_setup import gpt_api
load_dotenv()




class disco_api :

    intents = discord.Intents.all()
    bot = None

    def __init__(self, env_token):
        self.key = os.environ.get(env_token)
        intents = discord.Intents.all()
        self.bot = commands.Bot(command_prefix='$', intents=intents)
        self.message = "hi"



    def is_token_valid(self):
        # Check if the bot token is set
        if not self.key:
            print("Bot token is not set!")
            return False

        # Check if the bot token is a valid format
        if not self.key.startswith("Bot "):
            print("Bot token format is invalid!")
            return False

    def run(self):
        self.bot.run(self.key)

    def log_rnning(self):
        print('bot logged in as : {0.user}'.format(self.bot))

    def log_message (self, message):
        print(message)

    def log_context(self, context):
        print(context)

    def is_bot_message(self, message):
        if message.author == self.bot.user:
            return True
        else:
            return False

    async def on_message(self,gpt_ref, message,context):
        if self.is_bot_message(message):
            return

        response = await gpt_api.get_response(gpt_ref, message, context)
        channel = message.channel
        await gpt_api.send_message(gpt_ref, response, channel)






