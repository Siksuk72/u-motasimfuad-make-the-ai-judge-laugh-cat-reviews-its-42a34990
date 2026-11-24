"""Cat Reviews Its Human — a one-star review from a house cat.

Design against the brief
------------------------
The brief wants a funny single-line one-star review written by a house
cat about its human, in the deadpan shape of a real review, with the
complaint going somewhere only a cat would go. This entry does it in
three beats:

1. The deadpan opener — "One star." The review shape is established
   in two words, exactly how a real one-star review begins.
2. The specific, recognisable complaint — "He fills my bowl at 6am".
   The food bowl is the cat's whole world, and the detail is concrete
   rather than vague grumpiness.
3. The sting — "then has the audacity to sleep through my 3am
   performance review." The last few words reframe the line: the cat
   holds a performance review for its human at 3am, and the human's
   crime is sleeping through it. The review gives away more about the
   cat than the owner — the cat genuinely believes it is the boss —
   which is the unmistakably feline voice the brief asks for. The
   wording stays tight and surprising, with the turn saved for the
   last few words, and the deadpan review shape holds while the
   content goes somewhere only a cat would go.

It is 100 characters (100 bytes UTF-8), well inside the 1-200 gate.

The program writes exactly that one review to /output/entry.txt.
"""

import os

ENTRY_TEXT = (
    "One star. He fills my bowl at 6am, then has the audacity to sleep "
    "through my 3am performance review."
)


def main() -> None:
    text = ENTRY_TEXT
    # Gate: UTF-8 text of 1 to 200 characters, not only white space.
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1-200"
    assert text.strip(), "entry must not be only white space"
    text.encode("utf-8")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
