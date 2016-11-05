import discord
from discord.ext import commands
import random
from random import choice as randchoice
import os
from .utils import checks

class botmeme:
    """I love to meme."""

    def __init__(self, bot):
        self.bot = bot
        self.spicymemes = ["https://cdn.discordapp.com/attachments/138418500107501568/237773317245894657/IMG_1908.PNG", "https://cdn.discordapp.com/attachments/138418500107501568/237763557360402433/sOBD1IW.png", "https://gyazo.com/4c0e5dba012c2bb822942cb31729f074", "https://cdn.discordapp.com/attachments/138418500107501568/231926986237411329/IMG_1798.PNG", "https://cdn.discordapp.com/attachments/138418500107501568/236253148073689089/IMG_0677.JPG", "http://pastebin.com/h4sNQ6VV",
        "https://gyazo.com/ab1baec47f8c6c36aac22d928f389180", "https://gyazo.com/0a32ed1ffe7a106b2227df3cf2b11567", "https://gyazo.com/f0d0fd1730f5c11b2095594c484becdc", "https://gyazo.com/a479e446f4acfb2f7b481b0bf65e1f08",
        "https://gyazo.com/89c034def24de4e13daa778f2a8de3d1", "https://gyazo.com/5900af46602a3ac3b726c6ed5aff5ef4", "https://gyazo.com/004be101ebc134ca05a169fade095e3a", "https://gyazo.com/7bdff048e2393f854e8f6c73eb23b593", "https://gyazo.com/df501650caaaf97a10239d9dc87fb0e0", 
        "https://gyazo.com/b4f4a5eae5827fb60c9203529df9c5c3", "https://gyazo.com/403579e74566384a0eab857e67fb4f8c", "https://gyazo.com/f84cb1eb723109475ee64e36645f7b89", "https://gyazo.com/96b114b21120d2b935bcc147cb09c079", "https://gyazo.com/f7f1dc5412b0f58ac3cc903f53856375",
        "https://gyazo.com/97c73a1b6fa3e05425da43489e123c02", "https://gyazo.com/98b00548e37d86751ef043a1d97c411f", "https://gyazo.com/db561a913cfd4cf2efc0b2b7cdd1bb97", "https://gyazo.com/08a49d3a57563341c9d262416e51215d", "https://gyazo.com/6fab30f6acaae52f59392abca36a7b04"]
    @commands.command(pass_context=True)
    async def letsmeme(self, message):
        """Lets meme!"""

        #Your code will go here
        await self.bot.say("""```
This is the memeing command. \n 
    The command is triggered by the trigger word [M e m e] 
    When the trigger word is said I will choose a memer and 
    post it for everyone to see. \n
This command is still in the very alpha stage - Dom```""")
    
    async def automeme(self, message):
        user = message.author
        msg = message.content.split()
        channel = message.channel
            
        if "meme" in msg:
            await self.bot.send_message(channel, randchoice(self.spicymemes))


def setup(bot):
    n = botmeme(bot)
    bot.add_listener(n.automeme, "on_message")
    bot.add_cog(n)