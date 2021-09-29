import discord
import os
import re
import time
from dotenv import load_dotenv

# https://discordpy.readthedocs.io/en/latest/api.html

class DiscordKeywordBot(discord.Client):
    CACHE_TTL = 900
    CACHE_DICT = {}
    CACHE_NEXT_PURGE = int(time.time()) + 1800

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.channel.id == int(os.getenv("SOURCE_CHANNEL")):
            if re.match(os.getenv("REGEX_MATCH"), message.content, re.IGNORECASE):
                #DiscordKeywordBot.cache_purge()
                #if DiscordKeywordBot.cache_check(message.content):
                    chan_list = [x.strip() for x in os.getenv("DISCORD_CHANNELS").split(',')]
                    for channel_id in chan_list:
                        channel = client.get_channel(int(channel_id))
                        await channel.send(message.content)
                        # await channel.send("<@&801031075782197278> | " + message.content)
load_dotenv()
while True:
    try:
        client = DiscordKeywordBot()
        client.run(os.getenv("DISCORD_TOKEN"))
    except:
        print("Error Occurred... retrying")

