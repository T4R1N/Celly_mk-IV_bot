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
    await client.change_presence(activity=discord. Activity(type=discord.ActivityType.watching, name='you'))
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


    #Hey Celly,
    if 'heycelly' in user_message_nospace.lower() or 'hc' in user_message_nospace.lower():
        if 'help' in user_message_nospace.lower():
            await message.channel.send("Say 'Hey Celly' in order to begin a command.\n`Rickroll` -> does not rickroll you no matter what you do to it.\n`Charity` -> spits out a random charity to donate to.\n\nThese commands don't need 'Hey Celly'.\n\n`fart` -> Don't say this. It will subtract from the Puffhyu Score.\n`℗` -> Displays the current Puffhyu Score.\n`I love Puffhyu` -> Increases Puffhyu Score.\n`I hate Puffhyu` -> Decreases Puffhyu Score.")
            return
        if 'rickroll' in user_message_nospace.lower():
            if "don't" in user_message_nospace.lower() or "do not" in user_message_nospace.lower():
                await message.channel.send('If you say so.')
                return
            else:
                await message.channel.send('No.')
                return
        if 'charity' in user_message_nospace.lower():
            if "don't" in user_message_nospace.lower() or "do not" in user_message_nospace.lower():
                await message.channel.send("Fine. Be that way.") 
                return
            else:
                charities = ['https://www.stjude.org/donate/pm.html?sc_dcm=58700006946881490&sc_cid=kwp&sc_cat=b&&amount=x&msclkid=2e4dc908262714e0a38dab54b85c94d1&utm_source=bing&utm_medium=cpc&utm_campaign=M%20-%20Core%20Brand%20EX%20EL&utm_term=st%20jude%20donate&utm_content=PM_PR_Dig_Srch_PM_AO_US_Nat_MS_M-Ads_LF_-_-_-_SERP-Exct_Srch-B_-_-_-_Donate_-_EL_-_-_Srch&gclid=2e4dc908262714e0a38dab54b85c94d1&gclsrc=3p.ds','https://www.mercycorps.org/donate/crisis-ukraine-give-now','https://www.feedingamerica.org/ways-to-give']
                await message.channel.send(random.charities)
                return
          

    #Puffhyu Score

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