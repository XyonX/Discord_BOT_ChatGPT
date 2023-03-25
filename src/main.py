import discord
import os
import openai
import requests
from dotenv import load_dotenv
from discord.ext import commands
import discord_setup
from gtp_setup import gtp_api
from discord_setup import disco_api



load_dotenv()


gtp = gtp_api ('ChatGPT_API')
disco = disco_api('Discord_Api')


@disco.bot.event
async def on_ready():
    disco.log_rnning()

@disco.bot.event
async def on_message(message):
   await disco.on_message(gtp, message)

disco.run()




