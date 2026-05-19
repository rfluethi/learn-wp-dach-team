# Handbuch — Regelwerk

## Kurzbeschreibung

Dieser Ordner enthält das Regelwerk für unser Team-Handbuch — also die Festlegungen, **wie** wir Inhalte für das Handbuch erstellen und pflegen. Er richtet sich an Teammitglieder, die als Autor:innen oder Reviewer:innen am Handbuch mitwirken.

## Geltungsbereich

Das Regelwerk gilt für alle Seiten des Handbuchs, unabhängig vom Thema (Tools, Prozesse, Organisation, Rollen).

**Format:** Wir verfassen die Inhalte in Markdown und veröffentlichen sie auf einer WordPress-Seite.

## Dateien in diesem Verzeichnis

### Regelwerk

| Datei | Inhalt | Wann brauchst du sie? | Diátaxis-Typ |
|---|---|---|---|
| [Leitprinzipien des Handbuchs](leitprinzipien.md) | Zielgruppen, Grundsätze P1–P8 | Bevor du anfängst zu schreiben — als Orientierung | Explanation |
| [Inhaltstypen und Vorlagen](inhaltstypen-und-vorlagen.md) | Fünf Seitentypen, Aufbau, Aufklappbereiche, Vorlagen A–E | Wenn du eine neue Seite anlegst | Reference |
| [Schreibregeln und Markdown-Konventionen](schreibregeln-und-markdown.md) | Sprache, Stil, Terminologie, externe Dokus, Markdown | Beim Schreiben und Formatieren | Reference |
| [Erstellungs- und Pflegeprozess](erstellungs-und-pflegeprozess.md) | Schritte, Rollen, Pflege, Review-Checkliste | Beim Veröffentlichen, Reviewen oder Aktualisieren | How-to (Prozess) |
| [Glossar](glossar.md) | Zentrale Begriffsdefinitionen | Bei jeder Begriffsverwendung (erste Verwendung verlinken) | Reference |

### Skill-Entwurf

| Datei | Inhalt |
|---|---|
| [SKILL.md](WordPress-Training-Team-DACH/GitHub-Repo/learn-wp-dach-team/handbuch/Handbuch/SKILL.md) | Entwurf eines Skills `handbuch-autor`, der beim Erstellen, Überarbeiten, Aufteilen und Reviewen von Handbuch-Seiten unterstützt. Status: Entwurf zum Testen, Version 2. |

## Verlinkungs-Skizze

```text
                   README.md (Eingangsseite)
                          │
        ┌─────────┬───────┼─────────┬─────────┐
        ▼         ▼       ▼         ▼         ▼
 leitprinzipien   inhaltstypen-     schreibregeln-     erstellungs-
                  und-vorlagen      und-markdown       und-pflege-
                                                       prozess
        │         │       │         │         │
        └─────────┴───┬───┴─────────┴─────────┘
                      ▼
                 glossar.md
              (von allen verlinkt)
```

## Verbindlichkeit

* Die Regeln in [Schreibregeln und Markdown-Konventionen](schreibregeln-und-markdown.md) sind **verbindlich**.
* Die [Leitprinzipien](leitprinzipien.md) und Strukturvorgaben aus [Inhaltstypen und Vorlagen](inhaltstypen-und-vorlagen.md) gelten als Standardweg. Abweichungen begründen wir im Review.

## Verwendete Quellen und Standards

### Frameworks und Methoden

* [Diátaxis-Framework](https://diataxis.fr/) — Daniele Procida. Strukturansatz für Dokumentation (vier Inhaltstypen).
* [Progressive Disclosure](https://www.nngroup.com/articles/progressive-disclosure/) — Jakob Nielsen / Nielsen Norman Group. Prinzip zum Umgang mit komplexen Inhalten.

### Internationale Standards

* [ISO/IEC/IEEE 26514:2022](https://www.iso.org/standard/72657.html) — *Systems and software engineering, Design and development of information for users.* Anforderungen an Struktur, Inhalt und Format von Nutzerdokumentation.
* [ISO/IEC/IEEE 26515:2018](https://www.iso.org/standard/70880.html) — *Developing information for users in an agile environment.* Prozesse für agile Dokumentationsentwicklung.
* [IEC/IEEE 82079-1](https://www.iso.org/standard/71620.html) — *Preparation of information for use (instructions for use) of products, General principles and detailed requirements.*

### Deutsche Quellen

* [tekom-Leitlinie „Regelbasiertes Schreiben, Deutsch für die Technische Kommunikation"](https://www.tekom.de/fileadmin/tekom.de/Die_tekom/Publikationen/Leseproben/2013_RBS_Deutsch_fuer_die_TK_Leseprobe.pdf) — Leseprobe (PDF). Standard für deutschsprachige technische Texte.

### Praxisbeispiele zur Inspiration

* [Cloudflare Developer Docs](https://developers.cloudflare.com/) — setzt Diátaxis konsequent um.
* [GitLab Pajamas Design System, Progressive Disclosure](https://design.gitlab.com/patterns/progressive-disclosure/)

## Metadaten

*Verantwortliche Rolle: GitHub-Spezialist · Letzte Aktualisierung: 2026-05-03 · Letzte Prüfung: 2026-05-03*
