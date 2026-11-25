"""Entry for make.fun bounty "Roast Your Own Agent".

Entry text (129 characters, limit: at most 140 characters).
No trailing newline is written, per the bounty text format.
"""

import os

ENTRY = 'I asked my agent for one file. It opened twelve tools, agreed with itself twice, then summarised the meeting about that one file.'

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
