# bfd.py
**A simple API wrapper for botsfordiscord.com written in Python.**

## Installation

Install via pip (recommended)

    pip install bfd.py

## Features

* POST server count
* AUTOMATIC server count updating
* GET bot info
* GET global bot list
* GET bot list for a specific user
* GET widgets url
* SEARCH for bots

## Example Discord.py Rewrite cog


```Python
    import bfd
    import discord
    from discord.ext import commands


    class BotsForDiscord:
        def __init__(self, bot):
            self.bot = bot
            self.token = 'token'  # set this to your BFD token
            self.bfd = bfd.Client(self.bot, self.token)  # Create a Client instance
            self.bfd.start_loop()  # Posts the server count every 3 minutes

        @commands.command()
        async def botinfo(self, ctx, bot: discord.User): # unfiltered botinfo, you should not use this, it's shit but it shows the behavior
            info = await self.bfd.get_bot(bot.id)
            if info is None:
                await ctx.send("Can't find this bot on BFD")
                return

            embed = discord.Embed(title="BotInfo")
            for key, value in info.as_dict().items():
                if key == "" or value == "":
                    continue

                embed.add_field(name=key, value=str(value))

            await ctx.send(embed=embed)


    def setup(bot):
        bot.add_cog(BotsForDiscord(bot))
```

## Discussion, Support and Issues
For general support and discussion of this project, please join the Discord server: https://discord.gg/qyXqA7y \
[![Discord Server](https://discordapp.com/api/guilds/204663881799303168/widget.png?style=banner2)](https://discord.gg/qyXqA7y)

To check known bugs and see planned changes and features for this project, please see the GitHub issues.\
Found a bug we don't already have an issue for? Please report it in a new GitHub issue with as much detail as you can!