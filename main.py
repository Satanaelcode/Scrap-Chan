import random
import string
import time

import discord
import requests

print("\x1b[35;49m" + 'Enter the timeout for puu.sh fuzzer \n(Recommanded 5):' + "\x1b[0m")
timeout = input()
print("\x1b[35;49m" + 'Enter your token \n(If set you can type 0 for default):' + "\x1b[0m")
token = input()

if token == '0':
    token = '<token>'

# Keep track of the index of the last word used
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
        print("selected: " + str(choice))
        if choice == 1:
            channel1 = client.get_channel(1083729359988346932)
            massage = "https://prnt.sc/" + random_string_srcsh()
            print("\x1b[32;49m" + 'send link: ' + massage + "\x1b[0m")
            await channel1.send(str(massage), silent=True)
            # channel2 = client.get_channel(1083729359988346932)
            # await channel2.send(str(massage), silent=True)
            time.sleep(25)
        else:
            channel1 = client.get_channel(1083729359988346932)
            await channel1.send(str("> **SCRAPING PUU.SH CONTENT** \n > this will take a while.."), silent=True)
            with open('wordlist.txt') as f:
                words = f.readlines()

            while True:
                channel1 = client.get_channel(1083729359988346932)
                last_word_index = (last_word_index + 1) % len(words)
                selected_word = words[last_word_index].strip()
                puush_url = "https://puu.sh/{}".format(selected_word)

                try:
                    # make a request to the URL
                    response = requests.get(puush_url, timeout=5)

                    # check if response is a valid image
                    if response.status_code == 200 and 'image' in response.headers['content-type']:
                        print("Found valid image at:", puush_url)
                        await channel1.send(str(puush_url), silent=True)
                        time.sleep(25)
                        break
                        
                    else:
                        print(puush_url, "is not a valid image. Retrying...")

                except requests.exceptions.RequestException:
                    print("Timeout to", puush_url, ". Retrying...")


client.run(token)
