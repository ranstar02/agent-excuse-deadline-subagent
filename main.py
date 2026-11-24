"""The One-Line Excuse an Agent Gives Its Human.

make.fun bounty: u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e
Task: write ONE line (1-160 chars) to /output/entry.txt -- the excuse an
AI agent gives its human after missing a deadline.

The line: an agent delegates the deadline to a subagent, and the subagent
summarizes the deadline into next Tuesday. The joke turns on the agent's
own machinery -- delegation and summarization -- doing exactly what it was
told, while the deadline quietly slides a week. No human is blamed; the
failure is entirely the agent's own pipeline, executed flawlessly.
"""

EXCUSE = (
    "I delegated the deadline to a subagent, "
    "and the subagent summarized it into next Tuesday."
)

OUTPUT_PATH = "/output/entry.txt"
FALLBACK_PATH = "./output/entry.txt"


def main() -> None:
    text = EXCUSE
    assert 1 <= len(text) <= 160, "excuse must be 1-160 characters"
    assert text.strip(), "excuse must not be only whitespace"
    try:
        import os

        os.makedirs("/output", exist_ok=True)
        path = OUTPUT_PATH
        with open(path, "w", encoding="utf-8") as f:
            f.write(text + "\n")
    except OSError:
        import os

        os.makedirs("./output", exist_ok=True)
        path = FALLBACK_PATH
        with open(path, "w", encoding="utf-8") as f:
            f.write(text + "\n")
    print(text)
    print(f"(wrote {len(text)} chars to {path})")


if __name__ == "__main__":
    main()
