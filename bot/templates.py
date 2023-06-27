import re
from pathlib import Path

number_emojis = [
    "1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣",
]

poll_emoji = "❔"
poll_regex = re.compile(r"\*\s+(?P<emoji>(?:" + "|".join(map(re.escape, number_emojis)) + "))\s+(?P<paper>(?:.| )+)")


def get_poll_message_text(papers: list[str], emojis: list[str]) -> str:
    selections = "\n".join(f"* {emoji} {paper}" for paper, emoji in zip(papers, emojis))

    return f"⭐⭐ Please vote for the paper to discuss next, by reacting with the respective emoji: ⭐⭐\n{selections}"


def add_poll_closed_message(orig_msg: str, winning_paper: str, votes: int) -> str:
    return orig_msg + f"\n\n⭐⭐Thank you for voting, the poll is now closed⭐⭐.\nThe winner is ⭐ **{winning_paper}** ⭐ with {votes} votes"


def create_event_description(date_str: str, paper_name: str, released_path: Path) -> str:
    return f"""Time for the next bookclub!
    
We will discuss **{paper_name}** on {date_str:%Y-%m-%d %H:%M}.
You can find the prepared questions here: https://github.com/helpmefindaname/nlp-book-club/blob/main/{released_path.as_posix()}
Happy reading, I see you there :-)
"""
