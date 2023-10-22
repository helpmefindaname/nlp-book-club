import re
from datetime import datetime
from pathlib import Path

number_emojis = [
    "1️⃣",
    "2️⃣",
    "3️⃣",
    "4️⃣",
    "5️⃣",
    "6️⃣",
    "7️⃣",
    "8️⃣",
    "9️⃣",
]

date_poll_emoji = "📅"
poll_emoji = "❔"
poll_regex = re.compile(
    r"\*\s+(?P<emoji>(?:"
    + "|".join(map(re.escape, number_emojis))
    + "))\s+(?P<paper>(?:.| )+)"
)
date_poll_regex = re.compile(
    r"\*\s+(?P<emoji>(?:"
    + "|".join(map(re.escape, number_emojis))
    + "))\s+(?P<date>\d\d\d\d-\d\d-\d\d)"
)


def get_date_poll_message_text(dates: list[datetime], emojis: list[str]) -> str:
    selections = "\n".join(
        f"* {emoji} {dt.year:04}-{dt.month:02}-{dt.day:02} 19:00"
        for dt, emoji in zip(dates, emojis)
    )

    return f"⭐⭐ Please vote for the date to hold the next date, by reacting with the respective emoji: ⭐⭐\n{selections}"


def add_date_poll_closed_message(orig_msg: str, dt: datetime, votes: int) -> str:
    return (
        orig_msg
        + f"\n\n⭐⭐Thank you for voting, the poll is now closed⭐⭐.\nThe date is ⭐ **{dt.year:04}-{dt.month:02}-{dt.day:02}** ⭐ with {votes} votes"
    )


def get_poll_message_text(papers: list[str], emojis: list[str]) -> str:
    selections = "\n".join(f"* {emoji} {paper}" for paper, emoji in zip(papers, emojis))

    return f"⭐⭐ Please vote for the paper to discuss next, by reacting with the respective emoji: ⭐⭐\n{selections}"


def add_poll_closed_message(orig_msg: str, winning_paper: str, votes: int) -> str:
    return (
        orig_msg
        + f"\n\n⭐⭐Thank you for voting, the poll is now closed⭐⭐.\nThe winner is ⭐ **{winning_paper}** ⭐ with {votes} votes"
    )


def create_event_description(
    date_str: str, paper_name: str, released_path: Path
) -> str:
    return f"""Time for the next bookclub!
    
We will discuss **{paper_name}** on {date_str:%Y-%m-%d %H:%M}.
You can find the prepared questions here: https://github.com/helpmefindaname/nlp-book-club/blob/main/{released_path.as_posix()}
Happy reading, I see you there :-)
"""


def create_event_notification(date_str: str, paper_name: str, event_url: str) -> str:
    return f"""The next bookclub is decided!

We will discuss **{paper_name}** on {date_str:%Y-%m-%d %H:%M}.

Please join the event here: {event_url}
"""
