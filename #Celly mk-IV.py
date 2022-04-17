#Celly mk-IV
#Invite is 
#https://discord.com/oauth2/authorize?client_id=965016094454734848&permissions=534723950656&scope=bot

import discord
import random
import math


getpscore = open("/home/pi/Documents/T4/Python/pscores.txt",'r').readlines(1)


TOKEN = ''

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    fulluser = str(message.author)
    user_message = str(message.content)
    user_message_nospace = str(user_message.replace(' ', ''))
    channel = str(message.channel.name)
    getpscore = open("/home/pi/Documents/T4/Python/pscores.txt",'r').readlines(1)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    # if message.channel.name == 'general':
    #     if user_message.lower() == 'hello':
    #         await message.channel.send(f'Hello, {username}!')
    #         return
    #     elif user_message.lower() == 'bye':
    #         await message.channel.send(f'Goodbye, {username}!')
    #         return
    #     elif user_message.lower() == '!random':
    #         response = f'This is your random number: {random.randrange(1000000)}'
    #         await message.channel.send(response)
    #         return

    # if user_message.lower() == '!anywhere':
    #     await message.channel.send('This can be used anywhere!')
    #     return

    if 'fart' in user_message_nospace.lower():
        await message.channel.send(f'{fulluser} has been reported to Discord Staff for saying {user_message}. (Message contains the f-word). -1℗.')
        c = open("/home/pi/Documents/T4/Python/pscores.txt", 'r+')
        c.truncate(0)
        pscorea = int(getpscore[0])
        pscorea = pscorea - 1
        c.writelines(str(pscorea))
        return

    if user_message == '℗':
        pscoreb = getpscore[0].replace('\n', '')
        await message.channel.send(f'The current Puffhyu Score is {pscoreb}℗.') 


    if 'puffhyu' in user_message_nospace.lower():
        if 'hate' in user_message_nospace.lower():
            await message.channel.send(f'Bad work, citizen. The CPP disapproves of this behavior. -1℗.')
            f = open("/home/pi/Documents/T4/Python/pscores.txt", 'r+')
            f.truncate(0)
            pscorea = int(getpscore[0])
            pscorea = pscorea - 1
            f.writelines(str(pscorea))
            return
        elif 'love' in user_message_nospace.lower():
            await message.channel.send(f'Good work, citizen. The CPP applauds you for your behavior. +1℗.')
            g = open("/home/pi/Documents/T4/Python/pscores.txt", 'r+')
            g.truncate(0)
            pscorea = int(getpscore[0])
            pscorea = pscorea + 1
            g.writelines(str(pscorea))
            return



client.run(TOKEN)