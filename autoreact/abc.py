"""
MIT License

Copyright (c) 2024-present japandotorg

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from abc import ABC, ABCMeta, abstractmethod
from typing import Any

import discord
from redbot.core import Config, commands

from .cache import Cache

from redbot.core.bot import Red  # isort: skip


class CompositeMetaClass(commands.CogMeta, ABCMeta):
    pass


class MixinMeta(ABC, metaclass=CompositeMetaClass):
    bot: Red
    config: Config
    cache: Cache

    def __init__(self, *_args: Any) -> None:
        super().__init__(*_args)

    @abstractmethod
    def format_help_for_context(self, ctx: commands.Context) -> str: ...

    @abstractmethod
    async def wait_until_cog_ready(self) -> None: ...

    @abstractmethod
    async def do_autoreact(self, message: discord.Message) -> None: ...

    @abstractmethod
    async def do_autoreact_event(self, message: discord.Message, type: str) -> None: ...
