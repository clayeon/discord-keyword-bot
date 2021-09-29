# discord-keyword-bot
A Discord bot that listens to a channel for keywords and posts messages matching the keywords into another channel


# Requirements
* python3

# Installation
```
	$ pip install -r requirements.txt
```

# Usage

* Create a Discord Bot User - https://discordpy.readthedocs.io/en/stable/discord.html
* Copy .env.example to a new file called .env
* Modify the file to include your Bot Users token. (DISCORD_TOKEN)
* Modify the file to include the ID of the Source Channel (SOURCE_CHANNEL), and the Discord Channel (DISCORD_CHANNELS) you want to put the matched messages into
* Modify the file to include the Keywords (REGEX_MATCH) you want to use. Use | to split the words.

# Running the bot
```
cd discord-keyword-bot
python3 bot.py
```
