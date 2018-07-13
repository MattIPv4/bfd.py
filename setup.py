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

from setuptools import setup
import re

with open("requirements.txt", "r") as f:
    requirements = f.readlines()

with open("README.md", "r") as f:
    readme = f.read()

with open("bfd/__init__.py", "r") as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('version is not set')

setup(
    name="bfd.py",
    author="MattIPv4",
    url="https://github.com/MattIPv4/bfd.py/",
    version=version,
    packages=['bfd'],
    python_requires=">= 3.5",
    include_package_data=True,
    install_requires=requirements,
    description='A simple API wrapper for botsfordiscord.com written in Python.',
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords="api wrapper discord bot bots stats statistics",
    classifiers=(
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Programming Language :: Python :: 3",
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
    ),
    project_urls={
        'Funding': 'http://patreon.mattcowley.co.uk/',
        'Support': 'http://discord.mattcowley.co.uk/',
        'Source': 'https://github.com/MattIPv4/bfd.py/',
    },
)

# python3 setup.py sdist bdist_wheel bdist_egg
# python3 -m twine upload dist/*
