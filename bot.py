
import discord
import asyncio
from random import randint

with open("info.txt") as f:
    content = f.readlines()

pw = content[0]



#Methods
methodList = []
methodList.append("/nix --- prints a greeting in the channel and send a private message with all commands for NixxonBot")
methodList.append("/slap {username} --- Have NixxonBot send your target a slap (NOT YET IMPLEMENTED). Don't write a user, and it will slap a random person in the channel.")



















client = discord.Client()

@client.event
@asyncio.coroutine
def on_message(message):
	# if the bot wrote this message, then ignore it
	if message.author == client.user:
		return

	print("Message content: "+message.content)
	if message.content.startswith('/nix'):
		yield from client.send_message(message.author, 'NixxonBot --help:')
		for method in methodList:
			yield from client.send_message(message.author, method)

	elif message.content.startswith('/slap'):
		memberList = list(client.get_all_members())
		print(str(memberList) + " and length: " + str(len(memberList)))
		num = randint(0, len(memberList)-1)
		if memberList[num].nick is None:
			slappee = memberList[num]
		else:
			slappee = memberList[num].nick
		yield from client.send_message(message.channel, str(slappee) + " has been slapped by " + str(message.author))


@client.event
@asyncio.coroutine
def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

# infinite loop that checks for events
client.run("joervad@hotmail.com",pw)


print("NixxonBot logged out")


#C:\Users\nico\Documents\NixxonBot\bot.py pi@192.168.0.23:/home/pi