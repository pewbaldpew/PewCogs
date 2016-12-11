import discord
from discord.ext import commands

class NaopggSearch:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def find(self, ctx):
        """Lookup anyone on Na.op.gg!"""

        search_valid = str(ctx.message.content[len(ctx.prefix+ctx.command.name)+1:].lower())
        
        
        await self.bot.say("http://na.op.gg/summoner/userName=" + search_valid)

def setup(bot):
    bot.add_cog(NaopggSearch(bot))
