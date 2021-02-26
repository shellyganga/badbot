import discord
import os
import secret
import re

client = discord.Client()

banned_words = [
    "hash", "map", "hashmap", "h4sh", "m4p", "h@sh", "m@p"
]


@client.event
async def on_ready():
    print("{0.user} has joined the server and ready to roll!".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    x = re.search("h*sh", message)
    if(x):
        await message.channel.send("no. no more fking bad words. get out")
        return
    for word in banned_words:
        if word in message.content.lower():
            await message.delete()
            await message.channel.send("no. no more fking bad words. get out")
            return

client.run(secret.secret)
