import argparse
import asyncio
import enum
import os
import calendar
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

import discord
import pytz
from discord import TextChannel, Message, EntityType, PrivacyLevel, Guild

from bot.folders import backlog, events, root_path
from bot.templates import (
    number_emojis,
    poll_emoji,
    get_poll_message_text,
    poll_regex,
    add_poll_closed_message,
    create_event_description,
    date_poll_emoji,
    get_date_poll_message_text,
    add_date_poll_closed_message,
    date_poll_regex,
    create_event_notification,
)


class CmdEnum(str, enum.Enum):
    CREATE_POLLS = "create_polls"
    CREATE_EVENT = "create_event"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser("start_command")
    parser.add_argument("cmd", type=CmdEnum, choices=list(CmdEnum))
    return parser.parse_args()


class BookclubClient(discord.Client):
    def __init__(self, cmd: CmdEnum):
        intents = discord.Intents.default()
        self.cmd = cmd
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
        if self.cmd == CmdEnum.CREATE_POLLS:
            await self.create_papers_poll()
            await self.create_date_poll()

        if self.cmd == CmdEnum.CREATE_EVENT:
            paper, _ = await self.close_poll()
            date, _ = await self.close_date_poll()
            await self.announce_event(paper, date=date)
        await self.close()

    async def create_papers_poll(self):
        an = self.announcements_channel
        papers = [p.stem.replace("-", " ").title() for p in backlog.glob("*.md")]
        emojis = number_emojis
        papers = papers[: len(emojis)]
        emojis = emojis[: len(papers)]

        poll_message_text = get_poll_message_text(papers, emojis)

        message = await an.send(poll_message_text)
        for emoji in emojis:
            await message.add_reaction(emoji)
        await message.add_reaction(poll_emoji)

    def find_date_candidates(self) -> list[datetime]:
        cal = calendar.Calendar(0)
        today = datetime.today()
        month = cal.monthdatescalendar(today.year, today.month)
        last_week = month[-1]
        monday = last_week[0]
        wednesday = last_week[2]
        friday = last_week[4]
        if wednesday.month != today.month:
            wednesday = wednesday + timedelta(days=-7)
        if friday.month != today.month:
            friday = friday + timedelta(days=-7)

        return sorted(
            [datetime(d.year, d.month, d.day) for d in [monday, wednesday, friday]]
        )

    async def create_date_poll(self):
        an = self.announcements_channel
        dates = self.find_date_candidates()
        emojis = number_emojis
        dates = dates[: len(emojis)]
        emojis = emojis[: len(dates)]
        poll_message_text = get_date_poll_message_text(dates, emojis)

        message = await an.send(poll_message_text)
        for emoji in emojis:
            await message.add_reaction(emoji)
        await message.add_reaction(date_poll_emoji)

    async def find_poll_message(self) -> Optional[Message]:
        an = self.announcements_channel
        result_msg = None
        async for msg in an.history(limit=5):
            if result_msg is not None:
                continue
            if any(
                reaction.me and reaction.emoji == poll_emoji
                for reaction in msg.reactions
            ):
                result_msg = msg
        return result_msg

    async def find_date_poll_message(self) -> Optional[Message]:
        an = self.announcements_channel
        result_msg = None
        async for msg in an.history(limit=5):
            if result_msg is not None:
                continue
            if any(
                reaction.me and reaction.emoji == date_poll_emoji
                for reaction in msg.reactions
            ):
                result_msg = msg
        return result_msg

    async def close_date_poll(self) -> tuple[datetime, int]:
        poll_msg = await self.find_date_poll_message()
        if poll_msg is None:
            return datetime(1996, 21, 3), -1
        emoji_to_votes = {
            reaction.emoji: reaction.count
            for reaction in poll_msg.reactions
            if reaction.me and reaction.emoji in number_emojis
        }
        voted_papers = {
            m["date"]: emoji_to_votes.get(m["emoji"], 0)
            for m in date_poll_regex.finditer(poll_msg.content)
        }
        winning_date_str, winning_votes = max(voted_papers.items(), key=lambda x: x[1])
        year, month, day = map(int, winning_date_str.split("-"))
        winning_date = datetime(
            year, month, day, hour=19, minute=0, tzinfo=pytz.timezone("Europe/Vienna")
        )
        await poll_msg.edit(
            content=add_date_poll_closed_message(
                poll_msg.content, winning_date, winning_votes
            )
        )

        return winning_date, winning_votes

    async def close_poll(self) -> tuple[Path, int]:
        poll_msg = await self.find_poll_message()
        if poll_msg is None:
            return Path("."), -1
        emoji_to_votes = {
            reaction.emoji: reaction.count
            for reaction in poll_msg.reactions
            if reaction.me and reaction.emoji in number_emojis
        }
        paper_to_emoji = {
            m["paper"]: m["emoji"] for m in poll_regex.finditer(poll_msg.content)
        }

        voted_papers = [
            (
                p,
                emoji_to_votes.get(
                    paper_to_emoji.get(p.stem.replace("-", " ").title(), ""), 0
                ),
            )
            for p in backlog.glob("*.md")
        ]

        winning_path, winning_votes = max(voted_papers, key=lambda x: x[1])

        await poll_msg.edit(
            content=add_poll_closed_message(
                poll_msg.content,
                winning_path.stem.replace("-", " ").title(),
                winning_votes,
            )
        )

        return winning_path, winning_votes

    async def announce_event(self, paper_path: Path, date: datetime) -> None:
        date_str = f"{date.year:04}-{date.month:02}"
        paper_name = paper_path.stem.replace("-", " ").title()
        saved_path = events / f"{date_str}-{paper_path.name}"
        released_path = paper_path.replace(saved_path)
        vc = self.voice_channel
        g = self.guild
        event = await g.create_scheduled_event(
            name=f"NLP-Papers-Bookclub {date_str}",
            start_time=date,
            entity_type=EntityType.voice,
            privacy_level=PrivacyLevel.guild_only,
            channel=vc,
            description=create_event_description(
                date, paper_name, released_path.relative_to(root_path)
            ),
        )

        await self.announcements_channel.send(
            create_event_notification(date, paper_name, event.url)
        )


async def run_client(cmd: CmdEnum):
    client = BookclubClient(cmd)
    await client.start_run(os.environ["DISCORD_TOKEN"])
    del client


async def main():
    args = parse_args()
    await run_client(args.cmd)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
