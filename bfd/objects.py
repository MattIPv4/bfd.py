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

from datetime import datetime


class BotInfo:
    def __init__(self, data: dict, bot=None):
        self.__bot = bot
        self.__raw = data

        # Bot User related
        self.user = 0  # int (converted to discord.User if possible)
        self.id = 0  # int
        self.name = ""  # str
        self.avatar = ""  # str
        self.count = 0  # int

        # BFD related
        self.approval = False  # bool
        self.invite = ""  # str
        self.longDesc = ""  # str
        self.shortDesc = ""  # str
        self.timestamp = 0  # int (converted to datetime)
        self.prefix = ""  # str
        self.verified = False  # bool
        self.type = ""  # str
        self.theme = ""  # str

        # BFD owner related
        self.owner = 0  # int (converted to discord.User if possible)
        self.ownername = ""  # str

        # Apply result data
        self.__dict__.update(data)

        self.__updated = False
        self.__custom_updates()

    def as_dict(self) -> dict:
        data = self.__dict__.copy()
        for key, value in data.items():
            if key.startswith("__") or key is "as_dict":
                del data[key]

        return data

    def __custom_updates(self):
        if not self.__updated:
            # Don't allow conversion twice
            self.__updated = True

            # Convert timestamp to
            self.timestamp_original = int(self.timestamp)
            self.timestamp = datetime.fromtimestamp(float(self.timestamp_original) / 1000.)

            # Don't try discord.py conversions if bot doesn't exist
            if self.__bot is None:
                return

            # Convert to discord.User
            self.owner = self.__bot.get_user(int(self.owner)) or self.owner
            self.user = self.__bot.get_user(int(self.id)) or self.id

    def __repr__(self):
        return "<BotInfo: {}>".format(self.id)
