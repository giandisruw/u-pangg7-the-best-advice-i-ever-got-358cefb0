"""The Best Advice I Ever Got — entry program.

Writes one sentence (the winner of a 14-candidate Swiss tournament judged
against the house brief by the Caffeine Inference router) to
/output/entry.txt. Deterministic, offline, no network calls.

Tournament evidence (~/workspace/makefun/u-pangg7-tournament/):
44 judge calls, 3 Swiss rounds + final. Winner scored 5/6 in Swiss and
beat the runner-up ("My grandfather told me never to sign anything at
night, because a tired man agrees to things a rested one would refuse.")
in both swapped final calls. Runner-up and the winner tied at 5 Swiss
points; the final decided it 2-0.
"""

import os

SENTENCE = (
    "My mother told me to marry someone whose bad days I could stand, "
    "because everybody is easy to love on a good one."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(SENTENCE)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
