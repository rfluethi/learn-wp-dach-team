# Konzept: GitHub-basierte Sitzungsverwaltung

Das Learn WP DACH Team verwaltet Sitzungsplanung, Beschlussprotokolle und Aufgaben vollständig über GitHub Issues und ein Kanban Board.

---

## Kernprinzip: Ein Issue = eine Sitzung

Jede Sitzung wird als **ein einziges GitHub Issue** geführt:

- **Vor der Sitzung:** Das Issue ist die Traktandenliste
- **Nach der Sitzung:** Das Issue ist das Beschlussprotokoll

Aufgaben aus der Sitzung werden als eigene Issues im Kanban Board verwaltet.

---

## Sitzungsstruktur

Jede Sitzung folgt dieser festen Grundstruktur:

1. Begrüssung (+ ev. Vorstellungsrunde)
2. News: Was gibt es Neues in der WordPress-Welt?
3. Status offene Arbeiten
4. Status Projekte (Übersetzungen, Lektionen, Workshops)
5. Status Lerngruppen
6. Diskussionsthemen *(variabel, von Teammitgliedern vorgeschlagen)*

---

## Issue-Typen

| Typ | Label | Wofür |
|---|---|---|
| Sitzung | `sitzung` | Traktandenliste + Beschlussprotokoll |
| Traktandum | `traktandum` | Diskussionsthema für die nächste Sitzung vorschlagen |
| Aufgabe | `aufgabe` | Action Item mit Verantwortlichen und Fälligkeitsdatum |

---

## Workflow im Überblick

```
1 Woche vorher     Sitzung              Nach der Sitzung     Review (max. 3 Werktage)
──────────────     ───────              ────────────────     ───────────────────────
Moderator          Protokollführer      Status →             Team gibt OK
erstellt        →  füllt Beschlüsse  →  "Blockiert"       →  im Kommentar →
Sitzungs-Issue     und Aufgaben aus     Protokoll-Review       Issue wird
Board-Status:                           läuft                  geschlossen →
"In Arbeit"             │               (Timeout: 3 Werk-      Protokoll-Archiv
                        ▼               tage, dann direkt
                   Aufgaben-Issues      schliessen)
                   → Kanban Board
```

---

## Labels

| Label | Verwendung |
|---|---|
| `sitzung` | Meeting-Issues |
| `traktandum` | Vorgeschlagene Diskussionsthemen |
| `aufgabe` | Action Items / Tasks |
| `blockiert` | Aufgaben mit Blocker oder Abhängigkeit |
| `nächste-sitzung` | Vertage Themen für das nächste Meeting |
| `lerngruppe` | Themen rund um Lerngruppen |
| `webseite` | Themen rund um learn-wp-dach.org |
| `übersetzung` | Übersetzungsprojekte |
| `organisation` | Organisatorische Aufgaben |

---

## Kanban Board

**Projektname:** Learn WP DACH – Aufgaben

| Spalte | Inhalt |
|---|---|
| Traktanden | Vorgeschlagene Diskussionsthemen |
| Offen | Aufgaben, noch nicht begonnen |
| In Arbeit | Aufgaben aktiv in Bearbeitung |
| Blockiert | Aufgaben mit Blocker – oder Sitzungsprotokoll wartet auf Review |
| Erledigt | Abgeschlossene Aufgaben |

> Sitzungs-Issues erscheinen **nicht** im Kanban – sie sind das Protokoll-Archiv und werden über die Protokoll-View oder die Suche gefunden.

---

## Protokoll-Archiv

Alle geschlossenen Sitzungs-Issues sind dauerhaft abrufbar:
- **Suche:** Issues → Filter: `label:sitzung is:closed`
- **Protokoll-Index:** In der `README.md` wird automatisch eine Liste aller Protokolle geführt (via GitHub Actions)

---

## Weiterführende Dokumente

- [Benutzeranleitung](benutzeranleitung.md) – Schritt-für-Schritt-Anleitung für alle Teammitglieder
- [Setup-Anleitung](setup.md) – Technische Einrichtung (für Admins)
