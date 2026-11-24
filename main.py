"""One Line of Earned Pride — make.fun entry.

The line is built around one concrete payoff moment: Ana has spent three
winters hauling water up a hill in buckets, and this morning the new tap
finally works. The pride is never named or congratulated — it is earned
inside the line by the weight of the three winters, and it arrives at the
last words, when the water runs clear over her boots: the effort lands,
and the reader feels it land with her. No trophy, no podium, no
graduation — just a tap, a pair of boots, and a long job finished.
"""

import os

LINE = (
    "For three winters Ana hauled water up the hill in buckets; "
    "this morning she turned the new tap, and it sputtered, coughed, "
    "and ran clear over her boots."
)


def main() -> None:
    if not 1 <= len(LINE) <= 240:
        raise ValueError(f"line is {len(LINE)} characters, must be 1-240")
    if not LINE.strip():
        raise ValueError("line must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
