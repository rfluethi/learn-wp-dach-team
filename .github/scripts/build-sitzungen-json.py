#!/usr/bin/env python3
"""
Liest Issues mit Label 'sitzung' und erzeugt sitzungen.json
gemäß dem Schema aus dem Konzept.

Pfad-Empfehlung: .github/scripts/build-sitzungen-json.py
im Repo learn-wp-dach-team.

Aufruf:
    python3 build-sitzungen-json.py \\
        --input issues.json \\
        --repo owner/name \\
        --output sitzungen.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

# Schema-Version – bei Breaking Changes hochsetzen.
SCHEMA_VERSION = 1

# Titel-Format: "Sitzung 2026-04-28"
TITLE_DATE_RE = re.compile(r"Sitzung\s+(\d{4}-\d{2}-\d{2})")

# Im Body: **Uhrzeit:** 20:00 Uhr  ODER  ### Uhrzeit\n20:00
TIME_RE = re.compile(
    r"(?:\*\*Uhrzeit:?\*\*|###\s*Uhrzeit)\s*[:\n]?\s*(\d{1,2}:\d{2})",
    re.IGNORECASE,
)


def extract_session_date(title: str) -> str | None:
    """Liefert YYYY-MM-DD aus dem Titel oder None."""
    match = TITLE_DATE_RE.search(title or "")
    return match.group(1) if match else None


def extract_session_time(body: str) -> str:
    """Liefert HH:MM aus dem Body oder leerer String."""
    match = TIME_RE.search(body or "")
    if not match:
        return ""
    hh, mm = match.group(1).split(":")
    return f"{int(hh):02d}:{mm}"


def extract_minutes_date(closed_at: str | None) -> str:
    """Liefert YYYY-MM-DD aus closedAt oder leerer String."""
    if not closed_at:
        return ""
    try:
        # GitHub liefert ISO 8601 mit Z.
        dt = datetime.fromisoformat(closed_at.replace("Z", "+00:00"))
        return dt.date().isoformat()
    except ValueError:
        return ""


def build(issues: list[dict], repo: str) -> dict:
    """Baut die JSON-Struktur."""
    today = datetime.now(timezone.utc).date()

    next_candidates: list[dict] = []
    past: list[dict] = []

    for issue in issues:
        title = issue.get("title", "")
        session_date = extract_session_date(title)
        if not session_date:
            # Issue mit Label 'sitzung' ohne erkennbares Datum → überspringen.
            continue

        url = issue.get("url", "")
        # gh issue list (JSON) liefert State als "OPEN"/"CLOSED".
        state = (issue.get("state") or "").upper()
        body = issue.get("body", "") or ""

        try:
            session_date_obj = datetime.strptime(session_date, "%Y-%m-%d").date()
        except ValueError:
            continue

        is_future = session_date_obj >= today

        if state == "OPEN" and is_future:
            next_candidates.append(
                {
                    "title": title,
                    "session_date": session_date,
                    "session_time": extract_session_time(body),
                    "url": url,
                }
            )
        else:
            past.append(
                {
                    "title": title,
                    "session_date": session_date,
                    "minutes_date": extract_minutes_date(issue.get("closedAt")),
                    "url": url,
                }
            )

    # Nächste Sitzung: nächstgelegenes Datum gewinnt.
    next_session = None
    if next_candidates:
        next_candidates.sort(key=lambda s: s["session_date"])
        next_session = next_candidates[0]

    # Vergangenheit: absteigend nach session_date.
    past.sort(key=lambda s: s["session_date"], reverse=True)

    return {
        "schema_version": SCHEMA_VERSION,
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source_repo": repo,
        "next_session": next_session,
        "past_sessions": past,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Pfad zur Issues-JSON (gh issue list ...)")
    parser.add_argument("--repo", required=True, help="owner/name, z. B. rfluethi/learn-wp-dach-team")
    parser.add_argument("--output", required=True, help="Pfad zur Ausgabe-JSON")
    args = parser.parse_args()

    issues_path = Path(args.input)
    if not issues_path.exists():
        print(f"Input-Datei nicht gefunden: {issues_path}", file=sys.stderr)
        return 1

    with issues_path.open("r", encoding="utf-8") as fh:
        issues = json.load(fh)

    if not isinstance(issues, list):
        print("Erwarte JSON-Array von Issues.", file=sys.stderr)
        return 1

    payload = build(issues, args.repo)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    print(f"Geschrieben: {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
