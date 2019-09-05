import discord
from discord.ext import commands
import json
import asyncio

#Load json file with token
#fp = open("token.json")
#jsonFile = json.load(fp)
#fp.close()

PREFIX = '+'

class ChicoBot:
    """
    A bot created for the ChicoCA Discord Server
    """

    def __init__(self, token):
        self.token = token
        self.discord_client = commands.Bot(command_prefix=PREFIX)
        self.setup()

    def setup(self):
        @self.discord_client.event
        @asyncio.coroutine
        def on_ready():
            print("Online")
            print(f"Name: {self.discord_client.user.name}")
            print(f"ID: {self.discord_client.user.id}")
            yield from self.discord_client.change_presence(game=discord.Game(name='Serving Chico Since 1985'))

        @self.discord_client.event
        @asyncio.coroutine
        def on_message(message):
            if message.author.bot:
                return
            if message.content is None:
                print("Empty message received.")
                return
            print(f"Message: {str(message.content)}")

            if message.content.startswith(PREFIX):
                yield from self.discord_client.process_commands(message)

        ###SIMPLE HELLO COMMAND#####
        @self.discord_client.command(description="Says Hello", brief="Hello", aliases=['h'], pass_context=True)
        async def hello(context):
            await self.discord_client.say("Hello")

        ######NEWS COMMAND#########
        @self.discord_client.command(description="Posts news and articles into news chat",
                brief="News command",
                aliases=['n'],
                pass_context=True)
        async def news(context):
            channel_id = 373607739634745344
            channels = [i for i in self.discord_client.get_all_channels()]
            channel = None
            for chan in channels:
                if chan.name == "news-and-events":
                    channel = chan

            msg = ''.join([i + ' ' for i in context.message.content.split(" ")[1:]])
            msg += f"\nby {context.message.author.mention} in <#{context.message.channel.id}>"

            if channel is None:
                await self.discord_client.say(f"Failed to send to channel. Please try again or ping @ramsfield#7696 for assistance.")
            else:
                await self.discord_client.send_message(channel, content=f"{msg}")

        #########SAY COMMAND############
        @self.discord_client.command(description="Allows Ramsfield to do stuff. Idk, I don't make the rules",
                brief="Copycat",
                aliases=[],
                pass_context=True)
        async def say(context):
            if context.message.author.name != "Ramsfield":
                await self.discord_client.say(f"You're not my real dad!")
            else:
                await self.discord_client.say(''.join([i+' ' for i in context.message.content.split(' ')[1:]]))

    def run(self):
        self.discord_client.run(self.token)
