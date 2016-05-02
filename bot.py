
import discord
import asyncio

with open("info.txt") as f:
    content = f.readlines()

pw = content[0]

client = discord.Client()

@client.event
@asyncio.coroutine
def on_message(message):
        print("Message content: "+message.content)
        if message.content.startswith('/nix'):
                print("!hello seen")
                yield from client.send_message(message.channel, 'NixxonBot greets you.')

@client.event
@asyncio.coroutine
def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')

client.run("joervad@hotmail.com",pw)

print("NixxonBot logged out")
