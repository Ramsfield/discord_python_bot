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
            yield from self.discord_client.change_presence(game=discord.Game(name='Chico Bot'))
        
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

    def run(self):
        self.discord_client.run(self.token)
