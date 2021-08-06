import discord
import os
import requests
import json
from keep_alive import keep_alive

client = discord.Client()


@client.event
async def on_ready():
  print('We have logged in as {0.user}'
  .format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('!hei'):
    await message.channel.send('Hello!')


client.run 'TOKEN'
