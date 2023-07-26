import discord
import os
import openai
import requests
from dotenv import load_dotenv
from discord.ext import commands
import discord_setup
from gpt_setup import gpt_api
from discord_setup import disco_api



load_dotenv()


gpt = gpt_api ('ChatGPT_API')
disco = disco_api('Discord_Api')


@disco.bot.event
async def on_ready():
    disco.log_rnning()



@disco.bot.event
async def on_message(message):

    context = await gpt_api.get_context(gpt, message)
    await disco.on_message(gpt, message,context)

disco.run()




