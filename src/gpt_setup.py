import discord
import os
import openai
import requests
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()


class gpt_api:


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
        self.key = os.environ.get(env_api)
        self.headers = {"Authorization": f"Bearer {self.key}"}

    async def get_context(self,message):
        # Get the previous message if it exists
        context = ""
        async for m in message.channel.history(limit=2):
            if m.id != message.id:
                context = m.content
                break

        return context

    def set_payload(self,message,context):

        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "context", "content": context},
                {"role": "user", "content": message}
            ],
            "temperature": 0.5,
            "max_tokens": 60,
            "n": 1,
            "stop": "\n",
        }
        return payload

    async def get_response(self,message,context):
        self.payload =self.set_payload(message,context)

        response = requests.post(self.endpoint, headers=self.headers, json=self.payload)
        return response

    async def send_message(self, response, channel):

        if response.status_code == 200:
            response_text = response.json()['choices'][0]['message']['content']
            await channel.send(response_text)
        else:
            await channel.send("Error: Unable to get response from ChatGPT API.")

    def log_response(self, response):
        print('Responce Code : ', response.status_code)
        print('Responce  : ', response.text)





