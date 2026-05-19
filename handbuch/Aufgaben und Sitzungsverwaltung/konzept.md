# GitHub-basierte Sitzungsverwaltung

## Kurzbeschreibung

Diese Seite erklärt, **warum** das Learn WP DACH Team Sitzungsplanung, Beschlussprotokolle und Aufgaben über GitHub Issues und ein Kanban Board verwaltet, und welche Grundkonzepte dabei gelten.

## Worum geht es

Jede Sitzung wird als **ein einziges GitHub-Issue** geführt:

* **Vor der Sitzung** ist das Issue die Themenliste.
* **Nach der Sitzung** ist dasselbe Issue das Beschlussprotokoll.

Aufgaben aus der Sitzung werden als eigene Issues im Aufgaben-Board verwaltet. So entsteht aus jedem Beschluss ein nachverfolgbares Action Item.

## Warum machen wir das so

* **Single Source of Truth.** Themenliste und Protokoll an einem Ort verhindern, dass Beschlüsse in einem separaten Dokument verloren gehen.
* **Nachvollziehbarkeit.** GitHub protokolliert jede Änderung. Wer wann was geschrieben hat, ist transparent.
* **Verknüpfung.** Aufgaben-Issues lassen sich direkt mit dem Sitzungs-Issue ihrer Herkunft verknüpfen.
* **Niedrige Hürde.** GitHub-Accounts sind im Team ohnehin verbreitet. Ein zusätzliches Tool ist nicht nötig.

## Was bedeutet das für unsere Arbeit

### Sitzungsstruktur

Jede Sitzung folgt dieser Grundstruktur:

1. Begrüssung (gegebenenfalls Vorstellungsrunde)
2. News aus der WordPress-Welt
3. Status offene Arbeiten
4. Status Projekte (Übersetzungen, Lektionen, Workshops)
5. Status Lerngruppen
6. Diskussionsthemen (variabel, von Teammitgliedern vorgeschlagen)

### Übersicht: Issue-Typen

| Typ | Label | Zweck |
|---|---|---|
| Sitzung | `sitzung` | Themenliste und Beschlussprotokoll |
| Thema | `thema` | Diskussionsthema für die nächste Sitzung |
| Aufgabe | `aufgabe` | Action Item mit Verantwortlichen und Fälligkeit |

### Workflow im Überblick

```
1 Woche vorher     Sitzung              Nach der Sitzung     Review (max. 3 Werktage)
──────────────     ───────              ────────────────     ───────────────────────
Moderation         Protokollführung     Status →             Team gibt OK
erstellt        →  erfasst Beschlüsse → "Blockiert",      →  im Kommentar →
Sitzungs-Issue     und Aufgaben         Protokoll-Review     Issue wird
Board-Status                            läuft                geschlossen →
"In Arbeit"             │               (Timeout: 3 Werk-    Protokoll-Archiv
                        ▼               tage, dann direkt
                   Aufgaben-Issues      schliessen)
                   → Aufgaben-Board
```

### Übersicht: Labels

| Label | Verwendung |
|---|---|
| `sitzung` | Sitzungs-Issues |
| `thema` | Vorgeschlagene Diskussionsthemen |
| `aufgabe` | Action Items |
| `beschluss` | Themen, die zu einem formellen Entscheid geführt haben |
| `blockiert` | Aufgaben mit Blocker oder Abhängigkeit |
| `überprüfung` | Aufgabe erledigt, wartet auf Kontrolle |
| `nächste-sitzung` | Vertagte Themen |
| `lerngruppe` | Themen rund um Lerngruppen |
| `webseite` | Themen rund um learn-wp-dach.org |
| `übersetzung` | Übersetzungsprojekte |
| `organisation` | Organisatorische Aufgaben |

### Übersicht: Kanban-Spalten

Eine ausführliche Beschreibung der Spalten und Views findest du im [Aufgaben-Board](aufgaben-board.md). Kurzfassung:

* **Themen → Offen → In Arbeit → (ggf. Blockiert) → Überprüfung → Erledigt**
* Sitzungs-Issues erscheinen **nicht** im Board als reguläre Aufgaben. Sie sind über die View *Protokolle* auffindbar.

<details>
<summary>Hintergrund: Board-Status vs. Issue-Status</summary>

Der **Board-Status** (Spalte im Kanban) ist unabhängig vom **Issue-Status** (offen/geschlossen auf GitHub). Das ist Absicht: Ein Sitzungs-Issue ist während des Protokoll-Reviews zwar noch offen (Issue-Status), aber bereits in einem späten Stadium (Board-Status: *Blockiert* = wartet auf OK). Diese Trennung erlaubt eine differenzierte Statusführung, ohne dass das GitHub-Issue selbst geschlossen werden muss.

</details>

<details>
<summary>Hintergrund: Vier-Augen-Prinzip beim Protokoll</summary>

Bevor ein Sitzungs-Issue geschlossen wird, muss mindestens ein weiteres Teammitglied das Protokoll mit einem OK-Kommentar bestätigen. Damit ist sichergestellt, dass Beschlüsse nicht nur aus der Sicht der Protokollführung dokumentiert sind. Falls nach drei Werktagen kein OK eingeht, darf die Protokollführung das Issue trotzdem schliessen, mit Hinweis in der nächsten Sitzung. So bleibt der Prozess auch bei urlaubsbedingten Verzögerungen handlungsfähig.

</details>

## Verwandte Seiten

* [Thema vorschlagen](thema-vorschlagen.md)
* [Aufgabe erfassen](aufgabe-erfassen.md)
* [Sitzung durchführen](sitzung-durchfuehren.md)
* [Aufgaben-Board](aufgaben-board.md)
* [Häufige Fragen](haeufige-fragen.md)
* [Setup-Anleitung](setup.md) – technische Einrichtung (für Admins)

## Metadaten

*Verantwortliche Rolle: GitHub-Spezialist · Letzte Aktualisierung: 2026-05-03 · Letzte Prüfung: 2026-05-03*
