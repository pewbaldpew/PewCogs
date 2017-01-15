import discord
from discord.ext import commands

class Reposearch:
    """Search the approved repos for cogs."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=False)
    async def reposearch(self, ctx, *, repo: str=None):
        """You can use this command to search through the existing repos.
        This command will list all
        the existing cogs in each repo. This was all hard
        coded so I will try my best to keep it up to date. - Pew
        Do keep in mind these are case sensitive.\n
        Available repos: 26-Cogs, Squid-Plugins, Dumb-Cogs,
        Booru-Cogs, Jumper-Cogs, Mash-Cogs, PaddoCogs,
        CalebJ-Cogs, Refactored-Cogs, Eslyium-Cogs, Maybe-Useful-Cogs,
        Ax-Cogs, Palmtree5-Cogs, Ritsu-Cogs, Dusty-Cogs, tmerc-Cogs"""
        
        repo = ctx.message.content
        
        if "Squid-Plugins" in repo:
            await self.bot.say("https://github.com/tekulvw/Squid-Plugins\n Available Cogs:\n Admin - A collection of admin tools \n Autoapprove - Auto-Approve BOT account join requests \n Botinfo - Various bot information commands. \n Channelloger - Logs chat to file. \n Emotes - Twitch emotes for your servers. \n Karma - Award people with Karma points.\n Lastfm - LastFM Scrobbler \n Logger - Manage bot logging levels. \n Mentiontracker - Tracks your mentions when you're not online and sends you an alert when you get back. \n Nickometer - Measures the lameness of names \n Permissions - Custom command permissions \n Quotes - Save quotes and read them later \n Rss - Read RSS Feeds \n Rules - The Rules of the Internet \n Runescape - Basic Runescape commands \n Scheduler - Schedule commands to run once, or on repeat. \n Tickets - Allow users to create tickets for mods to read. \n Wikia - Basic wikia cog")
        elif "26-Cogs" in repo:
            await self.bot.say("https://github.com/Twentysix26/26-Cogs \n Available Cogs: \n Cleverbot - Talk with Cleverbot! \n Nomassmentions - Silences outcoming mass messages. \n Rift - Allows cross-server communication through Red \n Trigger - Create customizable triggers!")
        elif "Dumb-Cogs" in repo:
            await self.bot.say("https://github.com/irdumbs/Dumb-Cogs \n Available Cogs: \n Adventure - A text adventure game! \n Alot - Invites blots to your server. \n Economytrickle - Silently trickles economy.py's currency points to active users. \n Engine - The most basic cog example. \n Hal - Another useless gag cog parodying 2001: A Space Odyssey's HAL9000 \n Lolz - Translatez everythin teh bot sez into lolcat/lolspeak \n Ping - Pretty inaccurate pseudoping \n Repl - A modified REPL cog originally made by Danny \n Sadface - Simple example cog for on_message listeners/triggers \n Snacktime - Summon Snackburr")
        elif "Booru-Cogs" in repo:
            await self.bot.say("https://github.com/Alzarath/Booru-Cogs \n Available Cogs: Dan - Search https://danbooru.donmai.us/ for anime picture \n E621 - Search https://e621.net/ for furry pictures \n Gel - Search http://gelbooru.com/ for anime pictures \n Loli - Search https://lolibooru.moe/ for loli pictures \n Pony - Search https://derpibooru.org/ for pony pictures.")
        elif "Jumper-Cogs" in repo:
            await self.bot.say("https://github.com/Redjumpman/Jumper-Cogs \n Available Cogs: \n Animelist - Provides anime & manga info \n Casino - Casino system inspired by modded Economy \n Cookie - Steal and collect cookies. Who has the most cookies? \n Coupon - Creates coupons redeemable for points \n Dicetable - Can roll multiple die and outputs to a table \n Fortune - Gives a random fortune \n Heist - Heist mini-game inspired by Twitch's deep bot \n Language - Language dictionary that works with characters and alphabets \n Lottery - Can host lotteries for server users \n Pokedex - Returns movesets, locations, and more on Pokemon \n Raffle - Raffle system where you buy tickets with points \n Russianroulette - Play a game of russian roulette with up to 6 players \n Shop - Allows server owner to create a shop \n Tibia - Returns Tibia items/monsters/server info")
        elif "Mash-Cogs" in repo:
            await self.bot.say("https://github.com/Canule/Mash-Cogs \n Available Cogs: \n Bartender - Buy some drinks at the bar with Red's economy currency. \n Fourinarow - A four in a row game \n Freesound - Download SFX from freesound.org to the data/audio/sfx/freesound folder \n Indenticon - Generate an avatar based on your Discord ID. \n Imdb - Search for movies on imdb. \n Oboobs(NSFW) - NSFW - The oboobs/obutts.ru pictures of nature cog \n Omaps - Search for maps at openstreetmap.org \n Torrent - Search torrents at kickass/kat.cr for Linux distro's etc... \n Translated - Translate some text with use of translated.net. \n WeatherMs - A modified version of the community's weather cog. by rfilkins1992, Dex & Will. \n Wikipedia - Search for wikipedia articles\nRequires wikipedia module")
        elif "PaddoCogs" in repo:
            await self.bot.say("https://github.com/PaddoInWonderland/PaddoCogs \n Available Cogs: \n Away - Sets and unsets a user away. \n Barpm- Subscribe to beverages \n Calculator - Does math and stuff \n Caramba - ¡Ay, caramba! \n Customroles - Mods can add roles, users can apply or relievee roles. \n Games - Shows the most popular games played on a server. \n Goodreads - Search for a book on Goodreads \n Grenzpolizei - Be a despotic dictator and keep tabs on every member on the server. \n Invoice - Checks whether someone entered a voice channel. \n Kill - Have you always wanted to kill someone? If so, do it in a creative way! \n Konami - For anyone who enters the Konami code \n LastFM - Get information from Last.fm users. Such as last played songs and top artists. \n Logtools - Retrieve the logs from Discord neatly in a text file, slowly but sure \n Maolmao - LMAO Mao style \n Memes - Memes \n Oweather - Get weather information from Open Weather maps \n Quote - Quote someone with the message id \n Seen - Check when the user was last active on a server. \n Statistics - Keeps track of statistics \n Steam - Search for a game title on steam \n Wikipedia - Search Wikipedia \n Youtube - Search for videos on YouTube")
        elif "CalebJ-Cogs" in repo:
            await self.bot.say("https://github.com/neonobjclash/calebj-cogs \n Available Cogs: \n Activitylog - Logger for server and direct messages, attachments, and server changes. \n Customgcom - Define global custom commands. \n Datadog - Sends various bot statistics to a running statsd instance. \n Description - Set the bot description that shows in help \n Duel - Makes two users duel each other, with randomized moves and score tracking. \n Galias - Define global command aliases. \n Gallery - Automatically delete non-relevant posts in a gallery channel. \n Punish - Punish a misbehaving user. \n Purgepins - Delete pin notification messages after a per-channel interval. \n Recensor - Uses regular expressions to filter messages to delete, whether matching or non-matching. \n Serverquotes - Keep track of memorable quotes by server members or others. \n Sinfo - Includes commands to show basic info. \n Watchdog - Interacts with a systemd watchdog to ensure bot is up and connected at all times. \n Zalgo - Zalgoifies text. Put a number before the text to adjust intensity from 0-10.0")
        elif "Refactored-Cogs" in repo:
            await self.bot.say("https://github.com/Kowlin/refactored-cogs \n Available Cogs: \n Antilink - Automaticly remove Discord links from users \n Buyrole - Allow users to buy roles with Economy \n Google - Simply Google \n Massmove - Massmove users to another voice channel \n Punish - Punish a misbehaving user.")
        elif "Eslyium-Cogs" in repo:
            await self.bot.say("https://github.com/Eslyium/Eslyium-Cogs \n Available Cogs: \n Animal - Posts Cats/Pugs \n Doujin - Posts Random Doujin Links \n Feed - Forcefully feed a user. \n NSFW - NSFW Image Poster \n Slap - A Fun Cog That Allows You To Slap People With Items.")
        elif "Maybe-Useful-Cogs" in repo:
            await self.bot.say("https://github.com/AznStevy/Maybe-Useful-Cogs \n Available Cogs: \n Discomegle - Lets you chat with random people. \n Leveler - Increase activity(or not) on your server with chat exp! \n Markov - Generates a markov chain based on your server's chat \n Osu - Gives osu! profile information for all gamemodes. \n Whoplays - See who's playing what!")
        elif "Ax-Cogs" in repo:
            await self.bot.say("https://github.com/Aioxas/Ax-Cogs \n Available Cogs: \n Advgoogle - Retrieves results from Google \n Emote - Local emote summoning, has the ability to add, remove, or list emotes. Based on irdumb's sadface cog \n Geico - Online quote retrieval \n Horoscope - Zodiac and Chinese Horoscope and Fortune Cookie cog \n Strawpoll - Create a strawpoll")
        elif "Palmtree5-Cogs" in repo:
            await self.bot.say("https://github.com/palmtree5/palmtree5-cogs \n Available Cogs: \n Catfact - Gets a random cat fact via an api \n Conventry - Cog for making users only be able to talk to themselves \n Hpapi - Cog for getting info from the Hypixel API \n Mcsvr - Cog for getting Minecraft server status \n Reddit - Cog for getting stuff from Reddit \n Stream-hostcheck - Cog for setting hosted channel \n Ticketsystem - A ticket system inside of discord \n Tweets - Cog for getting info from Twitter")
        elif "Ritsu-Cogs" in repo:
            await self.bot.say("https://github.com/ritsu/RitsuCogs \n Available Cogs: \n Gnu - Some GNU inspired text utilities \n Sysinfo - Display system information \n Tokyotosho - TokyoTosho search and rss feed alerts")
        elif "Dusty-Cogs" in repo:
            await self.bot.say("https://github.com/Lunar-Dust/Dusty-Cogs \n Available Cogs: \n Autorole - Automatically adds a role to users who join your server. \n Desutils - Various utilities for debugging/server management. \n Greet - Plays a sound effect when a user joins a voice channel. \n Menu - A menu system based on reactions. \n Moji - Send a custom emoji from any server the bot is in. \n Pathfinder - Various features related to DnD/Pathfinder.")
        elif "tmerc-Cogs" in repo:
            await self.bot.say("https://github.com/tmercswims/tmerc-cogs \n Available Cogs: \n Catfact - Get random cat facts. \n Customjoinleave - Set a sound to play when a user joins a voice channel. \n Kz - Get kz stats \n Massdm - Send a direct message to all members of the specified Role. \n Memebership - Announces membership events. \n Playsound - Join, play a sound, and leave. \n Quotes - Store quotes, and get random ones. \n Randgame - Random games for your bot. \n Randimage - Displays a random image from a directory. \n Randimals - Displays random images of some animals. \n Reviewemoji - Submit and review emoji. \n Survey - Run surveys.")
        elif "Scarlet-Cogs" in repo:
            await self.bot.say("https://github.com/ScarletRav3n/Scarlet-Cogs \n Available Cogs: \n Fun - Random fun commands. \n Grammar - Corrects grammar mistakes. \n Kaomoji - Random Japanese emojis! \n Pepe - Random pepes")
            
def setup(bot):
    bot.add_cog(Reposearch(bot))
