import discord
import string
import random
import time

print('Type your token:')
token = input()

if token == '0':
    token = '<DEFAULT TOKEN HERE>'


def random_string():
    letters = string.ascii_lowercase
    digits = string.digits
    return ''.join(random.choice(letters) + random.choice(letters) + random.choice(digits) + random.choice(digits) + random.choice(digits) + random.choice(digits))


intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    while True:
        massage = "https://prnt.sc/" + random_string() 
        print('send link: ' + massage)
        channel = client.get_channel(1071803218063003658)
        # Send a message to the channel

        await channel.send(massage)
        time.sleep(25)


client.run(token)
