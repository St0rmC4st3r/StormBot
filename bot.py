import discord
import asyncio

client=discord.Client()



@client.event
async def on_ready():
    print('I have come!')
    
@client.event
async def on_message(message):
    if message.author.name+'#'+message.author.discriminator!='BuffDJ#9856':
        await client.add_reaction(message, "U+1F923")
    print(message.author.name+'@'+message.channel.name+': '+message.content)









client.run('MzQxMzQ1NzE4MTM4ODMwODY4.DS4lVg.JdBPXJdBPh59371x9ho_QHPDQTc')