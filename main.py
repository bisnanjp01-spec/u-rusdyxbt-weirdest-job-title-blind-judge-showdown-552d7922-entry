"""Weirdest Job Title: Blind Judge Showdown — entry program.

Writes one original job title, 60 characters or fewer and nothing else,
to /output/entry.txt, where the sealed scorer and the blind judge read it.

The title is a real-sounding job with one gloriously specific twist:
a senior whisperer — the kind of title a stable would print on a badge —
whose charges are the vending machines that swallowed your coins.
You can picture the person, toolbox in hand, talking a coin slot down.
"""

import os

TITLE = "Senior Whisperer to Vending Machines That Ate Your Money"


def main() -> None:
    if not (1 <= len(TITLE) <= 60):
        raise SystemExit(f"title must be 1-60 characters, got {len(TITLE)}")
    if not TITLE.strip():
        raise SystemExit("title must not be only white space")
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(TITLE)
    print(f"wrote entry ({len(TITLE)} characters) to {out_path}")


if __name__ == "__main__":
    main()
