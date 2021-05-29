import discord
import os
from dotenv import load_dotenv
import dao
import validator
from codes import ResponseCodes

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

    if message.content.startswith('!rate-addprof '):
        response = validator.add_prof_val(message.content)
        if response != ResponseCodes.OK:
            print('Message: "' + message.content + '" failed. ERROR: '+str(response))
            return
    
    if message.content.startswith('!rate-deleteprof '):
        response = validator.remove_prof_val(message.content)
        if response != ResponseCodes.OK:
            print('Message: "' + message.content + '" failed. ERROR: '+str(response))
            return
    
    if message.content.startswith('!rate-delete '):
        response = validator.remove_rating_val(message.content)
        if response != ResponseCodes.OK:
            print('Message: "' + message.content + '" failed. ERROR: '+str(response))
            return

    if message.content.startswith('!rate '):
        response = validator.rate_val(message.content)
        if response != ResponseCodes.OK:
            print('Message: "' + message.content + '" failed. ERROR: '+str(response))
            return
    
    if message.content.startswith('!rate-remove '):
        response = validator.remove_val(message.content)
        if response != ResponseCodes.OK:
            print('Message: "' + message.content + '" failed. ERROR: '+str(response))
            return


    
client.run(os.environ.get("TOKEN"))