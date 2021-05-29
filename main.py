import discord
import os
from dotenv import load_dotenv
import validator
from codes import ResponseCodes
import util

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
    if message.content == '!quit':
        await client.close()

    if message.content.startswith('!rate-addprof '):
        response = await validator.add_prof_val(message.content)
        if response != ResponseCodes.OK:
            print('Message: "' + message.content + '" failed. ERROR: '+str(response))
            return
        await util.rate_addprof(message.content)
        
    if message.content.startswith('!rate-deleteprof '):
        response = validator.remove_prof_val(message.content)
        if response != ResponseCodes.OK:
            print('Message: "' + message.content + '" failed. ERROR: '+str(response))
            return
        await util.rate_deleteprof(message.content)
    
    if message.content.startswith('!rate-delete '):
        response = await validator.remove_rating_val(message.content)
        if response != ResponseCodes.OK:
            print('Message: "' + message.content + '" failed. ERROR: '+str(response))
            return
        await util.rate_delete(message.content)

    if message.content.startswith('!rate '):
        response = await validator.rate_val(message.content)
        if response != ResponseCodes.OK:
            print('Message: "' + message.content + '" failed. ERROR: '+str(response))
            return
        await util.rate(message.content, message.author.mention)

client.run(os.environ.get("TOKEN"))