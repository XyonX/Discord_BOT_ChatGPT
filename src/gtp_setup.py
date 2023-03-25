import discord
import os
import openai
import requests
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()


class gtp_api:


    key = None
    endpoint = "https://api.openai.com/v1/chat/completions"
    headers = None
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": "default Message "}],
        "temperature": 0.5,
        "max_tokens": 60,
        "n": 1,
        "stop": "\n",
    }

    def __init__(self, env_api):
        self.key = os.environ.get('env_api')
        self.headers = {"Authorization": f"Bearer {self.key}"}

    def set_payload(self,message):

        self.payload = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": message}],
            "temperature": 0.5,
            "max_tokens": 60,
            "n": 1,
            "stop": "\n",
        }



