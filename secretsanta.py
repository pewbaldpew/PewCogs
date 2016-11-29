from .utils.dataIO import dataIO 
import discord
from discord.ext import commands
import os
import random
from .utils.dataIO import fileIO

class SecretSanta:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot
        self.sent = "data/secretsanta/sent.json"
        self.receive = "data/secretsanta/receive.json"

    @commands.command(pass_context=True, no_pm=True)
    async def assignpartner(self, ctx):
        """Sign up for Secret Santa today!"""

        #We need to load it each time the command is typed
        self.sent = fileIO("data/secretsanta/sent.json", "load")
        self.receive = fileIO("data/secretsanta/receive.json", "load")

        if ctx.message.author.id not in self.sent:
            self.sent.append(ctx.message.author.id)
            users_list = []
            for member in ctx.message.server.members:
                if member.id not in self.receive:
                    if member.id != ctx.message.author.id:
                        users_list.append([member.name, member.id])

            if len(users_list) != 0:
                secret_santa = random.choice(users_list)
                self.receive.append(secret_santa[1])

                fileIO("data/secretsanta/sent.json", "save", self.sent)
                fileIO("data/secretsanta/receive.json", "save", self.receive)

                await self.bot.send_message(ctx.message.author, "Your secret santa is {}, {}!".format(secret_santa[0], ctx.message.author.name))
            else:
                await self.bot.send_message(ctx.message.author, "Everybody has been already taken... :grimacing:")
        else:
            await self.bot.send_message(ctx.message.author, "Silly you, you have already signed up for secret santa")
        
def check_folder():
    if not os.path.exists("data/secretsanta"):
        print("Creating data/secretsanta folder...")
        os.makedirs("data/secretsanta")

def check_file():
    data = []
    h = "data/secretsanta/sent.json"
    if not dataIO.is_valid_json(h):
        print("Creating files")
        dataIO.save_json(h, data)

def check_file2():
    data = []
    f = "data/secretsanta/receive.json"
    if not dataIO.is_valid_json(f):
        print("Creating files")
        dataIO.save_json(f, data)

def setup(bot):
    check_folder()
    check_file()
    check_file2()
    bot.add_cog(SecretSanta(bot))
