import discord
import requests
import json
from bot_command import roll_dice
TOKEN = "*YOUR TOKEN*"

intents = discord.Intents.default()

intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        
    if message.content.startswith('$who'):
        await message.channel.send('Im puggy')
    
    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)
        
    if message.content.startswith('$roll'):
        roll1 = roll_dice()
        await message.channel.send(roll1)
    
    
    
    
    
        
        

