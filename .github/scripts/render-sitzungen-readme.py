#!/usr/bin/env python3
"""
Rendert den Sitzungs-Block in README.md aus sitzungen.json.

Erwartet sitzungen.json im Schema v2 (drei Listen: upcoming_sessions,
in_progress_sessions, past_sessions).

Ersetzt in README.md alles zwischen den Markern
    <!-- BEGIN SITZUNGEN -->
    <!-- END SITZUNGEN -->
durch eine generierte Übersicht.

Aufruf:
    python3 render-sitzungen-readme.py \\
        --json sitzungen.json \\
        --readme README.md
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

BEGIN_MARKER = "<!-- BEGIN SITZUNGEN -->"
END_MARKER = "<!-- END SITZUNGEN -->"


def fmt_date(iso: str) -> str:
    """YYYY-MM-DD → DD.MM.YYYY."""
    m = re.match(r"^(\d{4})-(\d{2})-(\d{2})$", iso or "")
    if not m:
        return iso or ""
    return f"{m.group(3)}.{m.group(2)}.{m.group(1)}"


def render_session_row_with_time(s: dict) -> str:
    """Zeile für upcoming/in_progress: Name | Datum | Uhrzeit."""
    title = s.get("title", "").strip() or "Sitzung"
    url = s.get("url", "")
    name_cell = f"[{title}]({url})" if url else title
    date_cell = fmt_date(s.get("session_date", ""))
    time_cell = s.get("session_time", "") or "—"
    return f"| {name_cell} | {date_cell} | {time_cell} |"


def render_past_row(s: dict) -> str:
    """Zeile für past_sessions: Name | Sitzungsdatum | Protokoll-Datum."""
    title = s.get("title", "").strip() or "Sitzung"
    url = s.get("url", "")
    name_cell = f"[{title}]({url})" if url else title
    date_cell = fmt_date(s.get("session_date", ""))
    minutes_cell = fmt_date(s.get("minutes_date", "")) or "—"
    return f"| {name_cell} | {date_cell} | {minutes_cell} |"


def render_block(data: dict) -> str:
    """Baut den kompletten Block, der zwischen den Markern landet."""
    parts: list[str] = []
    parts.append(BEGIN_MARKER)
    parts.append("<!-- Der Block zwischen den Markern wird automatisch von der GitHub Action")
    parts.append("     `sitzungen-json.yml` aus den Issues gepflegt. Nicht manuell editieren. -->")
    parts.append("")

    upcoming = data.get("upcoming_sessions") or []
    in_progress = data.get("in_progress_sessions") or []
    past = data.get("past_sessions") or []

    # Anstehende Sitzungen
    parts.append("### Anstehende Sitzungen")
    parts.append("")
    if upcoming:
        parts.append("| Veranstaltung | Datum | Uhrzeit |")
        parts.append("| --- | --- | --- |")
        for s in upcoming:
            parts.append(render_session_row_with_time(s))
    else:
        parts.append("_Aktuell keine anstehenden Sitzungen geplant._")
    parts.append("")

    # Sitzungen in Bearbeitung
    parts.append("### Sitzungen in Bearbeitung")
    parts.append("")
    if in_progress:
        parts.append("| Veranstaltung | Datum | Uhrzeit |")
        parts.append("| --- | --- | --- |")
        for s in in_progress:
            parts.append(render_session_row_with_time(s))
    else:
        parts.append("_Keine offenen Sitzungen mit vergangenem Datum._")
    parts.append("")

    # Protokolle (nach Jahr gruppiert, absteigend)
    parts.append("### Protokolle")
    parts.append("")
    if past:
        grouped: dict[str, list[dict]] = {}
        for s in past:
            year = (s.get("session_date") or "")[:4]
            if not year:
                continue
            grouped.setdefault(year, []).append(s)
        for year in sorted(grouped.keys(), reverse=True):
            sessions = sorted(
                grouped[year],
                key=lambda x: x.get("session_date", ""),
                reverse=True,
            )
            parts.append(f"#### {year}")
            parts.append("")
            parts.append("| Veranstaltung | Sitzung | Protokoll |")
            parts.append("| --- | --- | --- |")
            for s in sessions:
                parts.append(render_past_row(s))
            parts.append("")
    else:
        parts.append("_Noch keine Protokolle vorhanden._")
        parts.append("")

    # Footer: Datenstand
    generated_at = data.get("generated_at", "")
    if generated_at:
        # ISO 8601 (mit oder ohne Z) → sprechende Form
        ts = generated_at.replace("Z", "+00:00")
        try:
            dt = datetime.fromisoformat(ts)
            stand = dt.strftime("%d.%m.%Y, %H:%M UTC")
        except ValueError:
            stand = generated_at
        parts.append(f"_Stand: {stand} — automatisch generiert aus den Issues._")
        parts.append("")

    parts.append(END_MARKER)
    return "\n".join(parts)


def replace_block(readme: str, new_block: str) -> str:
    """Ersetzt den BEGIN/END-Block oder fällt auf den kompletten Sitzungen-Abschnitt zurück."""
    pattern = re.compile(
        re.escape(BEGIN_MARKER) + r".*?" + re.escape(END_MARKER),
        re.DOTALL,
    )
    if pattern.search(readme):
        return pattern.sub(new_block, readme)

    # Fallback für ältere README-Versionen ohne Marker:
    # Ersetze den kompletten Abschnitt "## Sitzungen" bis zur nächsten H2.
    section_pattern = re.compile(
        r"(^##\s+Sitzungen\s*$\n)(.*?)(?=^##\s+|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    replacement = r"\1\n" + new_block + "\n\n"
    if section_pattern.search(readme):
        return section_pattern.sub(replacement, readme, count=1)

    raise RuntimeError(
        "Weder Marker noch Abschnitt '## Sitzungen' in README gefunden. "
        "Bitte README-Struktur prüfen."
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", required=True, help="Pfad zur sitzungen.json")
    parser.add_argument("--readme", required=True, help="Pfad zur README.md")
    args = parser.parse_args()

    json_path = Path(args.json)
    if not json_path.exists():
        print(f"sitzungen.json nicht gefunden: {json_path}", file=sys.stderr)
        return 1

    with json_path.open("r", encoding="utf-8") as fh:
        data = json.load(fh)

    if (data.get("schema_version") or 0) != 2:
        print(
            f"WARN: schema_version != 2 ({data.get('schema_version')!r}). "
            "Render-Skript erwartet v2; Ergebnis ist evtl. unvollständig.",
            file=sys.stderr,
        )

    new_block = render_block(data)

    readme_path = Path(args.readme)
    if not readme_path.exists():
        print(f"README.md nicht gefunden: {readme_path}", file=sys.stderr)
        return 1

    with readme_path.open("r", encoding="utf-8") as fh:
        readme = fh.read()

    try:
        updated = replace_block(readme, new_block)
    except RuntimeError as e:
        print(str(e), file=sys.stderr)
        return 1

    if updated == readme:
        print("Keine Änderungen an der README nötig.")
        return 0

    with readme_path.open("w", encoding="utf-8") as fh:
        fh.write(updated)

    print(f"README aktualisiert: {readme_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
