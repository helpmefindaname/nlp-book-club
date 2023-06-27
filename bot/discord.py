import asyncio
import contextlib
import os
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

import discord
import pytz
from discord import TextChannel, Message, EntityType, PrivacyLevel, Guild

from bot.folders import backlog, events, root_path
from bot.templates import number_emojis, poll_emoji, get_poll_message_text, poll_regex, add_poll_closed_message, \
    create_event_description


class BookclubClient(discord.Client):

    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)

    @property
    def announcements_channel(self) -> TextChannel:
        for channel in self.get_all_channels():
            if channel.id == 1122319299860774962:
                return channel
        assert False

    @property
    def voice_channel(self) -> TextChannel:
        for channel in self.get_all_channels():
            if channel.id == 1122317295910404219:
                return channel
        assert False

    @property
    def guild(self) -> Guild:
        for g in self.guilds:
            if g.id == 1122317295088304271:
                return g
        assert False

    async def start_run(self, token: str):
        await self.login(token)
        await self.connect(reconnect=False)

    async def on_ready(self):
        paper, votes = await self.close_poll()
        await self.announce_event(paper, date=datetime.now().astimezone(pytz.timezone('Europe/Vienna')) + timedelta(days=1))
        await self.create_papers_poll()
        await self.close()

    async def create_papers_poll(self):
        an = self.announcements_channel
        papers = [p.stem.replace("-", " ").title() for p in backlog.glob("*.md")]
        emojis = number_emojis
        papers = papers[:len(emojis)]
        emojis = emojis[:len(papers)]

        poll_message_text = get_poll_message_text(papers, emojis)

        message = await an.send(poll_message_text)
        for emoji in emojis:
            await message.add_reaction(emoji)
        await message.add_reaction(poll_emoji)

    async def find_poll_message(self) -> Optional[Message]:
        an = self.announcements_channel
        result_msg = None
        async for msg in an.history(limit=5):
            if result_msg is not None:
                continue
            if any(reaction.me and reaction.emoji == poll_emoji for reaction in msg.reactions):
                result_msg = msg
        return result_msg

    async def close_poll(self) -> tuple[Path, int]:
        poll_msg = await self.find_poll_message()
        if poll_msg is None:
            return Path("."), -1
        emoji_to_votes = {
            reaction.emoji: reaction.count
            for reaction in poll_msg.reactions
            if reaction.me and reaction.emoji in number_emojis
        }
        paper_to_emoji = {m["paper"]: m["emoji"] for m in poll_regex.finditer(poll_msg.content)}

        voted_papers = [
            (p, emoji_to_votes.get(paper_to_emoji.get(p.stem.replace("-", " ").title(), ""), 0))
            for p in backlog.glob("*.md")
        ]

        winning_path, winning_votes = max(voted_papers, key=lambda x: x[1])

        await poll_msg.edit(content=add_poll_closed_message(
            poll_msg.content, winning_path.stem.replace("-", " ").title(), winning_votes)
        )

        return winning_path, winning_votes

    async def announce_event(self, paper_path: Path, date: datetime) -> None:
        date_str = f"{date.year:04}-{date.month:02}"
        paper_name = paper_path.stem.replace("-", " ").title()
        saved_path = events / f"{date_str}-{paper_path.name}"
        if True:
            released_path = saved_path
        else:
            released_path = paper_path.replace(saved_path)
        vc = self.voice_channel
        g = self.guild
        await g.create_scheduled_event(
            name=f"NLP-Papers-Bookclub {date_str}",
            start_time=date,
            entity_type=EntityType.voice,
            privacy_level=PrivacyLevel.guild_only,
            channel=vc,
            description=create_event_description(date, paper_name, released_path.relative_to(root_path))
        )


async def run_client():
    client = BookclubClient()
    await client.start_run(os.environ["DISCORD_TOKEN"])
    del client


async def main():
    await run_client()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
