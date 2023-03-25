import discord
import os
import openai
import requests
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()



class disco_api :

    intents = discord.Intents.all()
    bot = None


    def __init__(self, token):
        self.key = token
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

    def is_bot_message(self,message):
        if message.author == self.bot.user:
            return True
        else:
            return False

    async def on_message(self, message):
        if self.is_bot_message(message):
            return

        msg = message.content[1:]





