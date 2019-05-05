# Warning: bfd.py has been deprecated
 Please consider using [discordlists.py](https://github.com/MattIPv4/discordlists.py/) instead, this supports BFD as well as all other bot lists in a single module. It is also available on [PyPi](https://pypi.org/project/discordlists.py/).

<!-- Source: https://github.com/MattIPv4/template/blob/master/README.md -->

<!-- Title -->
<h1 align="center" id="bfdpy">
    bfd.py
</h1>

<!-- Tag line -->
<h3 align="center">A simple API wrapper for botsfordiscord.com written in Python.</h3>

<!-- Badges -->
<p align="center">
    <a href="https://pypi.org/project/bfd.py/" target="_blank">
        <img src="https://img.shields.io/pypi/v/bfd.py.svg?style=flat-square" alt="PyPi Version">
    </a>
    <a href="http://slack.mattcowley.co.uk/" target="_blank">
        <img src="https://img.shields.io/badge/slack-MattIPv4-blue.svg?style=flat-square" alt="Slack">
    </a>
</p>

----

<!-- Content -->
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
            self.bfd.start_loop()  # Posts the server count every 30 minutes

        @commands.command()
        async def botinfo(self, ctx, bot: discord.User): # unfiltered botinfo demo
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

<!-- Contributing -->
## Contributing

Contributions are always welcome to this project!\
Take a look at any existing issues on this repository for starting places to help contribute towards, or simply create your own new contribution to the project.

Please make sure to follow the existing standards within the project such as code styles, naming conventions and commenting/documentation.

When you are ready, simply create a pull request for your contribution and I will review it whenever I can!

Need to chat about the project and how you can get involved?\
Join the Slack workspace to find the appropriate channel, talk to other contributors and myself: [slack.mattcowley.co.uk](http://slack.mattcowley.co.uk)

<!-- Discussion & Support -->
## Discussion, Support and Issues

Need support with this project or have found an issue?
> Please check the project's issues page first!

Not found what you need?
* Create a GitHub issue here to report the situation, as much detail as you can!
* _or,_ You can join our Slack workspace to discuss the issue or to get support for the project:
<a href="http://slack.mattcowley.co.uk/" target="_blank">
    <img src="https://img.shields.io/badge/slack-MattIPv4-blue.svg?logo=slack&logoWidth=30&logoColor=blue&style=popout-square" alt="Slack" height="60">
</a>
