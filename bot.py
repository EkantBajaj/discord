import os
import random
from g_search import google_search
from presistence import update_history,show_history,setup_db

import discord

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    setup_db()
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome you can start by typing hi \n to search on google type !google <search term> \n to check recent search type !recent <term> enjoy!'
    )

@client.event
async def on_message(message):

    #To send Hey if user input hi or Hi or HI
    if message.content.lower() == 'hi':
        await message.channel.send('Hey')
        in_cmd = message.content


    #To filter out data and pass the search term to function google_search() and print links from raw data received
    elif message.content.split(" ",1)[0].lower() == '!google':
        results = google_search(message)
        await message.channel.send(f'Top 5 search result for {message.content.split(" ",1)[1]} are:')
        for result in results:
            await message.channel.send(f'{result}\n')
        update_history(message,message.content.split(" ",1)[1].lstrip())
    elif message.content[:7] == '!recent':
        search_term = message.content.split(" ",1)[1].lstrip()
        if search_term == '':
            await message.channel.send('Please mention what you are looking for like \n!recent google')
        if search_term != '':
            result = show_history(message, search_term)
            for dict in result:
                for item in dict:
                    await message.channel.send(item)


client.run(TOKEN)

