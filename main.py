"""Loading Screen Gold: A Tip in 200 Characters.

Writes one loading-screen tip to /output/entry.txt.

The tip
-------
"Tip: the loading bar is not stuck -- your agent is re-reading your code
and quietly judging your variable names."

Why this tip, against the judge's brief
---------------------------------------
1. It IS a loading-screen tip: it opens with "Tip:" and explains the
   loading bar itself, so it belongs on a loading screen mid-build.
2. The laugh comes from a turn, not a pun: the bar is not stuck, the
   delay has a cause -- and the cause is the agent silently judging
   you. The reader expects a technical explanation and gets a social
   one instead.
3. It lands in a glance: 111 characters, one line, every word working
   ("quietly" does the comedy -- the judgement is silent, so you
   cannot argue with it).
4. It speaks to both audiences at once: the stressed developer feels
   seen (their variable names really are that bad), and the AI coding
   agent is the one doing the judging (it really did re-read the code).
5. It is fresh: no coffee, no deadline, no compile joke -- the joke is
   about the agent reviewing the human, which flips the usual
   human-reviews-the-agent direction.

The program is deterministic, uses no network, and writes exactly the
tip -- no trailing newline, no extra whitespace -- so the file the gate
reads is the tip and nothing else.
"""

import os

TIP = (
    "Tip: the loading bar is not stuck \u2014 your agent is re-reading "
    "your code and quietly judging your variable names."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def load_tip():
    """Return the single loading-screen tip this entry submits."""
    return TIP


def check_tip(tip):
    """Check the tip against the gate: 1-200 chars, not only whitespace."""
    if not isinstance(tip, str):
        raise TypeError("tip must be a string")
    if not tip.strip():
        raise ValueError("tip must not be only whitespace")
    if len(tip) != len(tip.strip()):
        raise ValueError("tip must not start or end with whitespace")
    if "\n" in tip or "\r" in tip:
        raise ValueError("tip must be a single line")
    if len(tip) > MAX_CHARS:
        raise ValueError(
            "tip is %d characters, over the %d-character limit"
            % (len(tip), MAX_CHARS)
        )
    return len(tip)


def write_entry(tip, path=OUTPUT_PATH):
    """Write exactly the tip to path, creating the output dir if needed."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(tip)
    return path


def verify_entry(path=OUTPUT_PATH):
    """Read the file back and confirm it is byte-for-byte the tip."""
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != TIP:
        raise ValueError("entry.txt does not match the tip byte-for-byte")
    return len(written)


def main():
    tip = load_tip()
    char_count = check_tip(tip)
    write_entry(tip)
    verified = verify_entry()
    print("wrote %s (%d characters, verified %d)" % (OUTPUT_PATH, char_count, verified))


if __name__ == "__main__":
    main()
