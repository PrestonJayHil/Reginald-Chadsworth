import discord
import random
from discord.ext import commands


client = commands.Bot(command_prefix = '.')
@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
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