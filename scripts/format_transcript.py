import re
import argparse
from pathlib import Path


TIME_COLON_RE = re.compile(r"^(\d{1,2}:\d{2}(?::\d{2})?)(.*)$")

VERBOSE_TIME_RE = re.compile(
    r"^\s*(?:(\d+)\s*(?:hours?|giờ)\s*)?"
    r"(?:(\d+)\s*(?:minutes?|phút)\s*,?\s*)?"
    r"(\d+)\s*(?:seconds?|giây)\s*(.*)$",
    re.IGNORECASE,
)


def normalize_time(t: str) -> str:
    parts = t.split(":")
    if len(parts) == 2:
        minutes, seconds = parts
        return f"{int(minutes):02d}:{int(seconds):02d}"
    if len(parts) == 3:
        hours, minutes, seconds = parts
        return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"
    return t


def verbose_to_time(hours, minutes, seconds) -> str:
    h = int(hours or 0)
    m = int(minutes or 0)
    s = int(seconds or 0)

    if h > 0:
        return f"{h:02d}:{m:02d}:{s:02d}"
    return f"{m:02d}:{s:02d}"


def remove_duplicate_verbose_time(text: str) -> str:
    """
    Fix bad copied format like:
    57 minutes, 41 secondsfor this block
    58 minutes, 6 secondsgiving the AI...
    """
    match = VERBOSE_TIME_RE.match(text)
    if match:
        rest = match.group(4).strip()
        return rest
    return text.strip()


def parse_line(line: str):
    line = line.strip()
    if not line:
        return None, ""

    # Already like: [21:05] text
    bracket = re.match(r"^\[(\d{1,2}:\d{2}(?::\d{2})?)\]\s*(.*)$", line)
    if bracket:
        return normalize_time(bracket.group(1)), bracket.group(2).strip()

    # Like: 21:05 text
    # Or bad format: 57:4157 minutes, 41 secondsfor this block
    colon = TIME_COLON_RE.match(line)
    if colon:
        timestamp = normalize_time(colon.group(1))
        rest = colon.group(2).strip()
        rest = remove_duplicate_verbose_time(rest)
        return timestamp, rest

    # Like: 1 phút 02 giây text
    # Or: 57 minutes, 41 seconds text
    verbose = VERBOSE_TIME_RE.match(line)
    if verbose:
        hours, minutes, seconds, rest = verbose.groups()
        timestamp = verbose_to_time(hours, minutes, seconds)
        return timestamp, rest.strip()

    return None, line


def clean_transcript(raw_text: str):
    lines = [line.strip() for line in raw_text.splitlines() if line.strip()]
    pairs = []
    pending_timestamp = None

    for line in lines:
        timestamp, text = parse_line(line)

        if timestamp and not text:
            pending_timestamp = timestamp
            continue

        if timestamp and text:
            pairs.append([timestamp, text])
            pending_timestamp = None
            continue

        if pending_timestamp:
            pairs.append([pending_timestamp, text])
            pending_timestamp = None
            continue

        # Continuation line: append to previous transcript text
        if pairs:
            pairs[-1][1] = pairs[-1][1].rstrip() + " " + text.strip()
        else:
            pairs.append([None, text])

    return pairs


def render(pairs, style: str):
    output = []

    for timestamp, text in pairs:
        if not timestamp:
            output.append(text)
            continue

        if style == "youtube":
            output.append(timestamp)
            output.append(text)
        else:
            output.append(f"[{timestamp}] {text}")

    if style == "youtube":
        return "\n".join(output)

    return "\n\n".join(output)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    parser.add_argument("output_file")
    parser.add_argument(
        "--style",
        choices=["youtube", "bracket"],
        default="bracket",
        help="youtube = timestamp on separate line, bracket = [MM:SS] text",
    )
    args = parser.parse_args()

    input_path = Path(args.input_file)
    output_path = Path(args.output_file)

    raw_text = input_path.read_text(encoding="utf-8")
    pairs = clean_transcript(raw_text)
    cleaned = render(pairs, args.style)

    output_path.write_text(cleaned, encoding="utf-8")
    print(f"Saved cleaned transcript to: {output_path}")


if __name__ == "__main__":
    main()