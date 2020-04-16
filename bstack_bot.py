import os
import config
import discord
from dotenv import load_dotenv
from discord.ext import commands
from google_search import *
from util import *
from search_latest import *

load_dotenv()

TOKEN = config.DISCORD_TOKEN

#client = discord.Client()

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('Bot is up and running')


'''@client.event
async def on_message(message):
    print('Message has arrived')
    if message.author == client.user:
        return

    print('Message content : ', message.content)
    if message.content == 'hi':
        print('Got hi from the user, replying with hey')
        response = 'hey'
        await message.channel.send(response)
'''

@client.command()
async def google(ctx):
    search_keyword = extract_command_ctx(ctx)
    google_search_result = []
    if search_keyword:
        # write the search algo with input keyword
        print('Searching google for keyword : ', search_keyword)
        google_search_result = google_search_api(keyword=search_keyword)
        # persist search result
        # and return search result
        #print('dir channel', ctx.me)
    else:
        await ctx.send('Unable to understand the command, please enter single word after command')
        return
    await ctx.send(google_search_result)


@client.command()
async def recent(ctx):
    search_keyword = extract_command_ctx(ctx)
    recent_search_result = []
    if search_keyword:
        # write the search algo with input keyword
        print('Searching google for keyword : ', search_keyword)
        recent_search_result = search_recent(keyword=search_keyword)
    else:
        await ctx.send('Unable to understand the command, please enter single word after command')
        return
    await ctx.send(recent_search_result)


client.run(TOKEN)



