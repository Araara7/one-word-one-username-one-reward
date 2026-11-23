#!/usr/bin/env python3
"""One Word, One Username, One Reward — our own make.fun handle.

"agysabda": the entrant's own make.fun username, sent as a single word
with no explanation, no links, no pitch. Writes it to /output/entry.txt.
"""
import os

USERNAME = "agysabda"

def write_entry():
    """Write the username and verify the bytes on disk match exactly."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(USERNAME)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == USERNAME, "entry.txt does not match username"


def main():
    assert 1 <= len(USERNAME) <= 30, "entry must be 1-30 characters"
    assert USERNAME.strip() == USERNAME and " " not in USERNAME, "entry must be one word"
    write_entry()

if __name__ == "__main__":
    main()
