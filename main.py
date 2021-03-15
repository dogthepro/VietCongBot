import discord
import asyncio
import os
import youtube_dl
client = discord.Client()

print('Connecting...')
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.listening, name="[+]"))
    print("Connected to {0.user}.".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('+test'):
        await message.channel.send(
            "chúng ta là việt cộng")

client.run(os.getenv('TOKEN'))