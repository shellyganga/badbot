import discord
import os
import markovify
import secret

client = discord.Client()

banned_words = [
    "hash", "map", "hashmap", "h4sh", "m4p", "h@sh", "m@p"
]

with open("data/insults.txt", "r", encoding="utf-8") as f:
    text = f.read()
insult_model = markovify.NewlineText(text)
insult_model.compile()

with open("data/pickuplines.txt", "r", encoding="utf-8") as f:
    text = f.read()
pickup_model = markovify.NewlineText(text)
pickup_model.compile()

@client.event
async def on_ready():
    print("{0.user} has joined the server and ready to roll!".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    for word in banned_words:
        if word in message.content.lower():
            await message.delete()
            await message.channel.send("no. no more fking bad words. get out")
            return

    if message.content == "!insult":
        await message.channel.send(insult_model.make_sentence())
        return

    if message.content == "!pickup":
        await message.channel.send(pickup_model.make_sentence())
        return

client.run(secret.secret)