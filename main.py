import requests
import discord
import time
import os
from discord.ext import tasks, commands
import json
from datetime import datetime
from discord.utils import get
from discord.ext.commands import check, MissingRole, CommandError
intents = discord.Intents.all()
bot_config = json.loads(open("config.json", "r").read())
client = commands.Bot(command_prefix=bot_config["bot_prefix"],intents=intents)
channeltopost = bot_config["channel_id_to_send_boblox_updates"]


@client.event
async def on_ready():
	await client.change_presence(activity=discord.Game(name="Download JJSploit today. Level 7, no virus."))
	print("The Bot is online right now!")
	await my_loop.start()

@client.command(pass_context=True)
async def ping(ctx):
	await ctx.send("`Bot Ping: " + str(round(client.latency * 1000)) + "ms`")
    
    @client.command(aliases= 8
async def _8ball(ctx, *, question):
 responses = ['Yes!',
              'Yea no!',
              'Ofc!',
              'I guess?',
              'I dont want to answer.',
              'Nahhh.',
              'No i dont think so.',
              'Ask me this later.']
 await ctx.send(f'**__Question: {question}__** **__\nAnswer: {random.choice(responses)}__**')
    
        
@tasks.loop(seconds=60)
async def my_loop():
	a = requests.get('http://setup.roblox.com/version')
	time.sleep(10)
	b = requests.get('http://setup.roblox.com/version')
	if b.text not in a.text:
		channel = client.get_channel(channeltopost)
		embed = discord.Embed(title="Roblox just updated.:", description= "", color=0x00ff00)
		embed.add_field(name="Roblox Version", value="``"+b.text+"``", inline=True)
		embed.add_field(name="Last Version", value="``"+a.text+"``", inline=True)
		await channel.send(embed=embed)


@my_loop.before_loop
async def before_some_task():
  await client.wait_until_ready()



client.run('ODgwNTMwNzgxNzI0ODkzMTg0.YSfoMQ.X_xmZ4r26G4xF4z7U08o_1rxH30')