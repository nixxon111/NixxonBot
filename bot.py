#!/usr/bin/env python3
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
		args = message.content.split()
		print(str(args))
		print(str(len(args)))
		if len(args) == 1:
			memberList = list(client.get_all_members())
			print(str(memberList) + " and length: " + str(len(memberList)))
			num = randint(0, len(memberList)-1)
			if memberList[num].nick is None:
				slappee = memberList[num]
			else:
				slappee = memberList[num].nick
			yield from client.send_message(message.channel, str(slappee) + " has been slapped by " + str(message.author))
		elif len(args) == 2:
			memberList = list(client.get_all_members())
			print(str(memberList) + " and length: " + str(len(memberList)))
			for mem in memberList:
				if str(mem).lower() == str(args[1]).lower():
					yield from client.send_message(message.channel, str(mem) + " has been slapped by " + str(message.author))
					return
				elif mem.nick is not None:
					if mem.nick.lower() == str(args[1]).lower():
						yield from client.send_message(message.channel, str(mem.nick) + " has been slapped by " + str(message.author))
						return



		else:
			print("invalid /slap arguments" + message.content)


@client.event
@asyncio.coroutine
def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

client.run("joervad@hotmail.com", pw)
# infinite loop that checks for events


print("NixxonBot logged out")


#C:\pscp.exe C:\Users\nico\Documents\NixxonBot\bot.py pi@192.168.0.23:/home/discord_bot/

#Mossei and Syre use this (install pscp, comes with putty, write your own git repository location)
#C:\pscp.exe -P 32678 C:\Users\nico\Documents\NixxonBot\bot.py read@proxy54.yoics.net:/home/discord_bot/
#tmux a -t 0 (to detach from tmux session: "ctrl-B" followed by "D") //always run bot.py from tmux session "0"
#python3 /home/discord_bot/bot.py (to cancel script: "ctrl-C")
