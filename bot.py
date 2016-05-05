#!/usr/bin/env python3
import discord
import asyncio
from random import randint
from datetime import datetime, timedelta

with open("info.txt") as f:
    content = f.readlines()

pw = content[0]



#Methods
methodList = []
methodList.append("/nix --- send a private message with all commands for NixxonBot")
methodList.append("/slap {username} --- Have NixxonBot send your target a slap. Don't write a user, and it will slap a random person in the channel.")
methodList.append("/clock --- prints the time of day in the chat")

lonelyComments= []
lonelyComments.append("I feel alone.")
lonelyComments.append("Why no one write anything? :(")
lonelyComments.append("Please say hello to me...")
lonelyComments.append("Am I the only one here?")
lonelyComments.append("You guys are boring.")
lonelyComments.append("That lonely feeling...")

client = discord.Client()

lastMessage = datetime.now()
messageChannel = None

@client.event
@asyncio.coroutine
def on_message(message):
	# if the bot wrote this message, then ignore it
	messageChannel = message.channel
	if message.author == client.user:
		return

	print("Message content: "+message.content)

	lastMessage = datetime.now()
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
	elif message.content.startswith('/clock'):
		yield from client.send_message(message.channel, str(datetime.time(datetime.now()+timedelta(hours=2))))

@asyncio.coroutine
def lonely():
	yield from client.wait_until_ready()
	
	while not client.is_closed:
		if messageChannel is not None:
			if lastMessage is not None:
				if (lastMessage + timedelta(hours=4)) < datetime.now():
					yield from client.send_message(channel, lonelyComments[randint(0, len(lonelyComments)-1)])
		yield from asyncio.sleep(1300+randint(0,2800)) # task runs every ~4 hours (14400)

@client.event
@asyncio.coroutine
def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

# infinite loop that checks for events
loop = asyncio.get_event_loop()

try:
	loop.create_task(lonely())
	client.run("joervad@hotmail.com", pw)
	#loop.run_until_complete(client.login('token'))
	#loop.run_until_complete(client.connect())
except Exception:
	loop.run_until_complete(client.close())
finally:
	loop.close()

print("NixxonBot logged out")


#   C:\pscp.exe C:\Users\nico\Documents\NixxonBot\bot.py pi@192.168.0.23:/home/discord_bot/

#   Mossei and Syre use this (install pscp, comes with putty, write your own git repository location)
#   C:\pscp.exe -P 32678 C:\Users\nico\Documents\NixxonBot\bot.py read@proxy54.yoics.net:/home/discord_bot/
#   tmux a -t 0 (to detach from tmux session: "ctrl-B" followed by "D") //always run bot.py from tmux session "0"
#   python3 /home/discord_bot/bot.py (to cancel script: "ctrl-C")
