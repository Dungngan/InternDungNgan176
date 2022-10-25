from http import client
from urllib import response
import discord
from discord.ext import commands
import argparse
import random

Token ='MTAyODkyNjk2NDE4NDEzMzc0Mg.GlI525.QXvcSPHIifiC-B769--bm7VUHwaoKpTN79igOU'

client =discord.Client(intents=discord.Intents.default())
#bot =commands.Bot(command_prefix="cat")
@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))
# @client.command(name='hello')
# async def SendMessage(ctx):
#     await ctx.send('hello!')

@client.event
async def on_message(message):
    username=str(message.author).split('#')[0]
    user_message =str(message.content)
    channel =str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author ==client.user:
        return

    if message.channel.name =='test':
        if user_message.lower()=='':
            await message.channel.send(f'Hello {username}!')
            await message.channel.send('working!',file =discord.File('upanh.jpg'))
            return
        
    
client.run(Token)
