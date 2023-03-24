import discord
import os
import openai
import requests
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', intents=intents)




# ChatGPT API endpoint
#chatgpt_endpoint = "https://api.openai.com/v1/chat/completions"
chatgpt_endpoint="https://api.openai.com/v1/chat/completions"

# ChatGPT API access token
chatgpt_api_key = os.environ.get('ChatGPT_API')
print("chat gtp api key :" ,chatgpt_api_key )


@bot.event
async def on_ready():
    print('bot logged in as : {0.user}'.format(bot))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Check if message starts with command prefix
    if message.content.startswith('$'):
        # Get message content after the command prefix
        msg = message.content[1:]

        # Send message to ChatGPT API
        headers = {"Authorization": f"Bearer {chatgpt_api_key}"}
        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": msg}],
            "temperature": 0.5,
            "max_tokens": 60,
            "n": 1,
            "stop": "\n",

        }
        response = requests.post(chatgpt_endpoint, headers=headers, json=payload)
        print('Responce Code : ', response.status_code)
        print('Responce  : ', response.text)
        # Get response from ChatGPT API
        if response.status_code == 200:
            data = response.json()
            #response_text = data['choices'][0]['text']
            response_text = response.json()['choices'][0]['message']['content']
            await message.channel.send(response_text)
        else:
            await message.channel.send("Error: Unable to get response from ChatGPT API.")
    else:
        await bot.process_commands(message)



api_key = os.environ.get('Discord_Api')
bot.run(api_key)




