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

import aiohttp
from typing import Union

from .exceptions import *


class HttpClient:
    """
    This class is used to directly interact with the BFD API via http requests.

    Parameters
    ==========

    authorization : str
        A valid BFD API authorization token
    base : str
        The base url to use for the api
    """

    def __init__(self, authorization: str, base: str):
        self.authorization = authorization  # API authorization token
        self.base = base  # API base url
        self.session = None  # aiohttp session

    def _session_init(self):
        if self.session is None:
            self.session = aiohttp.ClientSession()

    @property
    def headers(self):
        return {'authorization': self.authorization, 'content-type': 'application/json'}

    def _handle_status_codes(self, status: int):
        if status == 401:
            raise Unauthorized("Check your token")

    async def _handle_response(self, resp: aiohttp.ClientResponse) -> dict:
        status, reason, json = resp.status, resp.reason, await resp.json()
        if json == {}:
            raise EmptyResponse()

        if status == 200:
            return json

        self._handle_status_codes(status)
        raise RequestFailure(status, reason)

    async def post(self, endpoint: str, content: Union[list, dict]) -> dict:
        """
        Post data to an API endpoint

        Parameter
        ========

        endpoint: str
            The endpoint to access on the API

        content: Union[list, dict]
            The data to be posted to the endpoint
        """
        self._session_init()
        async with self.session.post(url=self.base + endpoint, json=content, headers=self.headers) as resp:
            return await self._handle_response(resp)

    async def get(self, endpoint: str) -> dict:
        """
        Get data from an API endpoint

        Parameter
        ========

        endpoint: str
            The endpoint to access on the API

        Returns
        =======

        json: dict
            The response (if any) from the API endpoint
        """
        self._session_init()
        async with self.session.get(url=self.base + endpoint, headers=self.headers) as resp:
            return await self._handle_response(resp)

    async def post_guild_count(self, bot_id: int, guild_count: int) -> dict:
        """
        Post a server/guild count for a bot

        Parameter
        ========

        bot_id: int
            The id of the bot you want to update server/guild count for

        guild_count: int
            The server/guild count for the bot

        Returns
        =======

        json: dict
            The response (if any) from the API endpoint
        """
        return await self.post("bots/{}".format(bot_id), {"count": guild_count})
