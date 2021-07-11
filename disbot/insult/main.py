import os
import discord
import random
from discord.ext import commands
import asyncio
from datetime import datetime
from dotenv import load_dotenv
import traceback
import yaml
import io
from discord.ext import tasks
import requests
from discord import Webhook, AsyncWebhookAdapter
import aiohttp
from dhooks import Webhook as dhook

print(discord.__version__)
intents = discord.Intents.default() #sets up the intents obj
intents.members = True #flips the member inperwhatever it is to true
TOKEN = None

#load_dotenv()
#TOKEN = os.getenv('DISCORD_TOKEN') #retrieves the stuff needed from a *hidden* env file yall aint gettin

with open('token.yaml') as file:
	documents = yaml.full_load(file)
	for key, value in documents.items():
		if key == 'token': TOKEN = value
	if TOKEN == None: raise ValueError(f'Token not found, please check the file {file}')


bot = commands.Bot(command_prefix='!', intents=intents) #initilizes the bot]
bot.token = TOKEN

#flavorie text to make sure its working good
@bot.event
async def on_ready(): #initilization

    #guild = discord.utils.get(bot.guilds, name='bot tester') #gets the guild that i put in to kinda add some flavor text

    disp_guild = ''
    for x in bot.guilds:
        disp_guild += f'{x.name} ({x.member_count} members)\n'
        #await x.me.edit(nick = 'the amogus bot')

    print(
    	f'{bot.user} is connected to the following guilds:\n'
        f'{disp_guild}'
    )

    await bot.change_presence(activity=discord.Game(name='insutling x people')) #:)
    
@tasks.loop(seconds=600) #every 10 minutes
async def truth(self): #just the truth man
    await self.bot.wait_until_ready() #something something keeps the loop from breaking
    me = self.bot.get_user(661044029110091776) #gets my main acct
    await me.send('you\'re useless dude') #dms the truth

bot.run(TOKEN)