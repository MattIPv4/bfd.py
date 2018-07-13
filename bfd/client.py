"""
 *  bfd.py: A simple API wrapper for botsfordiscord.com written in Python.
 *  <https://github.com/MattIPv4/bfd.py/>
 *  Copyright (C) 2018 Matt Cowley (MattIPv4) (me@mattcowley.co.uk)
 *
 *  This program is free software: you can redistribute it and/or modify
 *   it under the terms of the GNU Affero General Public License as published
 *   by the Free Software Foundation, either version 3 of the License, or
 *   (at your option) any later version.
 *  This program is distributed in the hope that it will be useful,
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *   GNU General Public License for more details.
 *  You should have received a copy of the GNU Affero General Public License
 *   along with this program. If not, please see
 *   <https://github.com/MattIPv4/bfd.py/blob/master/LICENSE> or <http://www.gnu.org/licenses/>.
"""

import asyncio
from typing import Union, List

from .http import HttpClient
from .objects import BotInfo

API_VERSION = "v1"
API_BASE = "https://botsfordiscord.com/api/{}/".format(API_VERSION)


class Client:
    """
    This class is used to interact with the BFD API using a discord.py bot instance.

    Parameters
    ==========

    bot :
        An instance of a discord.py Bot or Client object
    token : str
        A valid BFD API Token
    interval : int[Optional]
        Seconds between each automatic posting of server/guild count. Defaults to 30 minutes
    base : str[Optional]
        The base url to use for the api. Defaults to API_BASE (https://botsfordiscord.com/api/v1/)
    """

    def __init__(self, bot, token: str, interval: int = 30 * 60, base: str = API_BASE):
        self.bot = bot
        self.base = base
        self.http = HttpClient(token, base)
        self.interval = interval

    @property
    def guild_count(self) -> int:
        """
        Gets the guild count from the bot

        Returns
        =======

        count: int
            The current number of guilds the bot is in
        """
        try:
            count = len(self.bot.guilds)
        except AttributeError:
            count = len(self.bot.servers)

        return count

    @property
    def server_count(self) -> int:
        """
        Gets the server count from the bot

        Returns
        =======

        count: int
            The current number of servers the bot is in
        """
        return self.guild_count

    @property
    async def bot_info(self) -> Union[None, BotInfo]:
        """
        Get the botinfo about the connected bot

        Returns
        =======

        bot: BotInfo
            Information about the connected bot
        """
        return await self.get_bot(self.bot.user.id)

    async def search_for_bots(self, **kwargs) -> List[BotInfo]:
        """
        Get bots fitting the specified parameters from BFD

        Parameter
        =========

        kwargs :
            A list of filters, e.g. name="Restarter v2", verified=True

        Returns
        =======

        bots: list(BotInfo)
            A list of information about the bots on bfd
        """

        def check_bot(bot):
            for key, value in kwargs.items():
                if not bot.__dict__.get(key) == value:
                    return False

                return True

        bots = await self.get_bots()
        return list(filter(check_bot, bots))

    async def get_bots(self, owner_id: int = None) -> List[BotInfo]:
        """
        Get all bots listed on BFD

        Parameter
        =========

        owner_id: int[Optional]
            The id of the user the bot should belong to

        Returns
        =======

        bots: list(BotInfo)
            A list of information about the bots on bfd
        """
        bots = [BotInfo(raw_info) for raw_info in await self.http.get("bots") if raw_info is not None]
        if owner_id is not None:
            bots = list(filter(lambda b: int(b.owner) == owner_id, bots))

        return bots

    async def get_bot(self, bot_id: int) -> Union[None, BotInfo]:
        """
        Get info for a bot on BFD

        Parameter
        =========

        bot_id: int
            The id of the bot you want to look up

        Returns
        =======

        bot: BotInfo
            Information about the bot
        """
        bot = await self.http.get("bots/{}".format(bot_id))
        return None if bot is None else BotInfo(bot)

    async def get_embed_url(self, bot_id: int) -> str:
        """
        Get the embed url of a bot on BFD

        Parameter
        ========

        bot_id: int
            The id of the bot you want to look up

        Returns
        ======
        embed_url: str
            The embed url of the bot
        """
        return "{}bots/{}/embed".format(self.base, bot_id)

    async def post_count(self) -> dict:
        """
        Post current server/guild count based on bot data to BFD

        Returns
        =======

        json: dict
            The response (if any) from the API endpoint
        """
        return await self.http.post_guild_count(self.bot.user.id, self.guild_count)

    def start_loop(self):
        """Start a loop that automatically updates the server/guild count for the bot on BFD"""
        self.bot.loop.create_task(self._loop(self.interval))

    async def _loop(self, interval):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            await self.post_count()
            await asyncio.sleep(interval)
