import discord
import os
from dotenv import load_dotenv

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

    if message.content.startswith('!add '):
        if message.guild.id not in grocery_lists:
            grocery_lists[message.guild.id] = []
        grocery_lists[message.guild.id].append(message.content[5:])
        await message.channel.send('Added {0} to the list!'.format(message.content[5:]))

    elif message.content == '!list':
        if message.guild.id not in grocery_lists or len(grocery_lists[message.guild.id]) == 0:
            return
        list = ''
        for index,item in enumerate(grocery_lists[message.guild.id]):
            list = list + str(index + 1)+'. '+item+'\n'
        await message.channel.send(list)

    elif message.content == '!clear':
        if message.guild.id not in grocery_lists:
            return
        grocery_lists[message.guild.id].clear()
        await message.channel.send('List cleared!')

    elif message.content.startswith('!remove '):
        if message.guild.id not in grocery_lists:
            return
        item = message.content[8:]
        if item in grocery_lists[message.guild.id]:
            grocery_lists[message.guild.id].remove(item)
            await message.channel.send('{0} removed from list!'.format(message.content[8:]))
        else:
            await message.channel.send('{0} is not on the list!'.format(message.content[8:]))
client.run(os.environ.get("TOKEN"))