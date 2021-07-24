import discord 
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '.')
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event(aliases=['8ball', 'test'])
async def ball(ctx, *, question):
    answers = [
            'It is for sure',
            'Definitely, So',
            'Yes',
            'No',
            'Hmm... uncertain',
            'Ask again, later',
            'All signs point to yes',
            'Concentrate and ask again',
            'Do not count on it',
            'My reply is no',
            'Outlook not so good',
            'Outlook good' ]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(answers)}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello, good sir.')

    if message.content.startswith('$introduce yourself'):
        await message.channel.send('Hello, I am Sir. Reginald Chadsworth, the discord butler.')

    
        
# provide token here 
client.run('')






















