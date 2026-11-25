"""Unsent: The Micro-Confession Sprint.

Emits a single two-part micro-confession to /output/entry.txt: first the
addressee line, then the unsent line itself, exactly as it was typed.
Standard library only; no network access; the same bytes every run.
"""

import os

RECIPIENT = "To: my Year 9 teacher"

# The confession is kept as short clauses so the one line stays readable
# in source while the program still writes it as a single line.
UNSAID_FRAGMENTS = [
    "I stole the answer key, not the quiet boy you expelled,",
    "and I stayed quiet because your praise was the first thing",
    "I ever wanted to keep.",
]

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def build_entry() -> str:
    """Assemble the two-part text, one line per part, trailing newline."""
    unsent_line = " ".join(UNSAID_FRAGMENTS)
    return "\n".join([RECIPIENT, unsent_line]) + "\n"


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as handle:
        handle.write(build_entry())


if __name__ == "__main__":
    main()
