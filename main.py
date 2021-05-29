import discord
import os
from dotenv import load_dotenv
import dao

load_dotenv()
grocery_lists = {}
client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as "+str(client.user))

@client.event
async def on_message(message):
    if not message.content.startswith('!'):
        return
    # if message.content == '!quit':
    #     await client.close()

    if message.content.startswith('!rate-add '):
        print(message.content[10:])
        await message.channel.send('Added {0} to the list!'.format(message.content[10:]))
    
    
    

    
client.run(os.environ.get("TOKEN"))