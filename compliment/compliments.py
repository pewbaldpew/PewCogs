import discord
import random
from discord.ext import commands


class Compliment:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def compliment(self, ctx):
        """Compliment a user!"""

        a = ["You're a beautiful person, friend.", "I hope you succeed in life.", "You're a bright human being and nobody can tell you otherwise.", "You have beautiful eyes.", "Your significant other will be a model, no doubt.", 
        "You will be very rich in the future. God bless you.", "DJ Khalid has nothing on you.", "You have the keys to success. You just haven't found them yet.", "You can be anything you want to be.", "Your smile is contagious.",
        "You look great today.", "You're a smart cookie.", "I bet you make babies smile.", "You have impeccable manners.", "I like your style.", "You have the best laugh.", "I appreciate you.", "You are the most perfect you there is.",
        "You are enough.", "You're strong.", "Your perspective is refreshing.", "You're an awesome friend.", "You light up the room.", "You deserve a hug right now.", "You should be proud of yourself.", "You're more helpful than you realize.",
        "You have a great sense of humor.", "You've got all the right moves!", "Is that your picture next to charming in the dictionary?", "Your kindness is a balm to all who encounter it.", "You're all that and a super-size bag of chips.", 
        "You're all that and a super-size bag of chips.", "You are brave.", "You're unlucky if you get this one. Fuck you kill yourself ape.", "You're even more beautiful on the inside than you are on the outside.", "You have the courage of your convictions.", 
        "Your eyes are breathtaking.", "If cartoon bluebirds were real, a bunch of them would be sitting on your shoulders singing right now.", "You are making a difference.", "You're like sunshine on a rainy day.", "You bring out the best in other people.", 
        "Your ability to recall random factoids at just the right time is impressive.", "You're a great listener.", "How is it that you always look great, even in sweatpants?", "Everything would be better if more people were like you!"]
        await self.bot.say(random.choice(list(ctx.message.server.members)).mention)
        await self.bot.say(random.choice(a))

        #Your code will go here
def setup(bot):
    bot.add_cog(Compliment(bot))
