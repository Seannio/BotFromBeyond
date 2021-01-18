###### Great Old One Bot made to use Markov Generation ######
import discord
import random
import markovify
import csv

# Token setup 
TOKEN = 'Njk2ODY2NjU0Mzc4MDAwNTE0.Xou-Ow.AeKpqluEziS_ZcSkd5Bw3oi1TIM'
client = discord.Client()

# Open the giant text file!
with open("corpus.txt") as f:  
    text = f.read()
    model = markovify.Text(text)

# Bot Setup / Profile
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    await client.change_presence(status=discord.Status.online, activity = discord.Activity(name='with the fragile minds of mortals.', type=discord.ActivityType.streaming))

# Text returns! 
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Main markov chain generator. Mostly worthless. 
    if message.content == '$summon':
        response = model.make_short_sentence(450) # Change this to edit length of return. Kinda' broken. 
        await message.channel.send(response)
    
    if "Cthulhu" in message.content:
        response = "Ph'nglui mglw'nafh Cthulhu R'lyeh wgah'nagl fhtagn!"
        await message.channel.send(response)

    if message.content == "$help":
        response = """```md
# YOU DARE REQUEST HELP
# Use '$' to preceed commands! 
< summon > | Generates a shitty markov chain from every Lovecraft work. 
```"""
        await message.channel.send(response)

client.run(TOKEN)
