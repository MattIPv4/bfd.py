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


class BFDException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class RequestFailure(BFDException):
    def __init__(self, status: int, reason: str):
        super().__init__("{}: {}".format(status, reason))


class Unauthorized(BFDException):
    def __init__(self, message=""):
        super().__init__(message)


class EmptyResponse(BFDException):
    def __init__(self):
        super().__init__("No response was received from the API")
