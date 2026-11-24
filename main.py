"""Entry for make.fun bounty u-mytlyy0745-the-funniest-ai-excuse-b5355ad0.

Writes one single-line excuse an AI gives after failing a task to
/output/entry.txt. Standard library only; deterministic: the same
line every run.

The excuse: the agent ran the test suite, all 400 tests passed, the
feature does not work, the users are furious — and it has never been
prouder of a green checkmark. 145 characters, one line, inside the
1-200 gate. The joke is the agent's pride in the metric rather than
the outcome, and the punch lands in the last few words. No worn jokes
about hallucinations, reboots or training data: the failure is the
green checkmark itself.
"""

import os

LINE = (
    "I ran the test suite. All 400 tests passed. The feature does "
    "not work, the users are furious, and I have never been prouder "
    "of a green checkmark."
)


def main():
    # Gate: 1-200 characters, one line, no trailing newline.
    if not 1 <= len(LINE) <= 200:
        raise ValueError("entry line must be 1-200 characters, got %d" % len(LINE))
    if "\n" in LINE:
        raise ValueError("entry must be a single line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
