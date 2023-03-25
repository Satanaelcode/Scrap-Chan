import random
import string
import time

import discord

print('Type your token:')
token = input()

if token == '0':
    token = '<DEFAULT TOKEN>'

## keep track of the index of the last word used
last_word_index = -1


def random_string_srcsh():
    letters = string.ascii_lowercase
    digits = string.digits
    return ''.join(
        random.choice(letters) + random.choice(letters) + random.choice(digits) + random.choice(digits) + random.choice(
            digits) + random.choice(digits))

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    global last_word_index
    while True:

        choice = random.randint(0, 1)
        ## ignore that...
        # print(str(choice) + ":debug.selected")
        if choice == 1:
            massage = "https://prnt.sc/" + random_string_srcsh()
            print('send link: ' + massage)
            channel1 = client.get_channel(<CHANNELID1>)
            await channel1.send(str(massage), silent=True)
            ## WORK IN PROGRESS
            # channel2 = client.get_channel(<CHANNELID2>)
            # await channel2.send(str(massage), silent=True)
            time.sleep(25)
        else:

            with open('wordlist.txt') as f:
                words = f.readlines()

            ## Use the last_word_index to select the next word sequentially
            last_word_index = (last_word_index + 1) % len(words)
            selected_word = words[last_word_index].strip()

            massage = "https://puu.sh/{}".format(selected_word)
            print('send link: ' + massage)
            channel1 = client.get_channel(CHANNELID1)
            await channel1.send(str(massage), silent=True)
            time.sleep(25)


client.run(token)
