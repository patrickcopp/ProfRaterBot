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

    elif message.content.startswith('!rate-addprof '):
        response = await validator.add_prof_val(message.content)
        if response != ResponseCodes.OK:
            print('Message: "' + message.content + '" failed. ERROR: '+str(response))
            await message.reply(str(response))
            return
        await util.rate_addprof(message.content)
        await message.reply('{0} {1} added to professor list!'.format(message.content.split()[1],message.content.split()[2]))
        
    elif message.content.startswith('!rate-deleteprof '):
        response = validator.remove_prof_val(message.content)
        if response != ResponseCodes.OK:
            print('Message: "' + message.content + '" failed. ERROR: '+str(response))
            await message.reply(str(response))
            return
        await util.rate_deleteprof(message.content)
        await message.reply('{0} removed from professor list!'.format(message.content.split()[1]))

    elif message.content.startswith('!rate-delete '):
        response = await validator.remove_rating_val(message.content)
        if response != ResponseCodes.OK:
            print('Message: "' + message.content + '" failed. ERROR: '+str(response))
            await message.reply(str(response))
            return
        await util.rate_delete(message.content)
        await message.reply('{0}\'s rating of {1} has been removed!'.format(message.content.split()[1], message.content.split()[2]))

    elif message.content.startswith('!rate '):
        response = await validator.rate_val(message.content)
        if response != ResponseCodes.OK:
            print('Message: "' + message.content + '" failed. ERROR: '+str(response))
            await message.reply(str(response))
            return
        await util.rate(message.content, message.author.mention)
        await message.reply('Your rating of {0} has been added!'.format(message.content.split()[1]))
    
    elif message.content.startswith('!rate-get '):
        response = await validator.get_rate_val(message.content)
        if response != ResponseCodes.OK:
            print('Message: "' + message.content + '" failed. ERROR: '+str(response))
            await message.reply(str(response))
            return
        rating = await util.rate_getratings(message.content)
        await message.reply('Prof. {0} rating: quality = {1}, difficulty = {2}, marks received = {2}!'.format(message.content.split()[1], rating['quality'], rating['difficulty'], rating['grade']))

client.run(os.environ.get("TOKEN"))