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

1. Begrüßung (gegebenenfalls Vorstellungsrunde)
2. News aus der WordPress-Welt
3. Status offene Arbeiten
4. Status Projekte (Übersetzungen, Lektionen, Workshops)
5. Status Lerngruppen
6. Diskussionsthemen (variabel, von Teammitgliedern vorgeschlagen)

### Wo die Details stehen

* **Issue-Typen und Labels:** vollständige Referenz unter [Issue-Typen und Labels](issue-typen-und-labels.md).
* **Ablauf einer Sitzung:** Schritte, Rollen und Workflow-Diagramm unter [Sitzung durchführen](sitzung-durchfuehren.md).
* **Kanban-Spalten und Views:** unter [Aufgaben-Board](aufgaben-board.md). Sitzungs-Issues erscheinen **nicht** im Board als reguläre Aufgaben; sie sind über die View *Protokolle* auffindbar.

<details>
<summary>Hintergrund: Board-Status vs. Issue-Status</summary>

Der **Board-Status** (Spalte im Kanban) ist unabhängig vom **Issue-Status** (offen/geschlossen auf GitHub). Das ist Absicht: Ein Sitzungs-Issue ist während des Protokoll-Reviews zwar noch offen (Issue-Status), aber bereits in einem späten Stadium (Board-Status: *Blockiert* = wartet auf OK). Diese Trennung erlaubt eine differenzierte Statusführung, ohne dass das GitHub-Issue selbst geschlossen werden muss.

</details>

<details>
<summary>Hintergrund: Vier-Augen-Prinzip beim Protokoll</summary>

Bevor ein Sitzungs-Issue geschlossen wird, muss mindestens ein weiteres Teammitglied das Protokoll mit einem OK-Kommentar bestätigen. Damit ist sichergestellt, dass Beschlüsse nicht nur aus der Sicht der Protokollführung dokumentiert sind. Falls nach drei Werktagen kein OK eingeht, darf die Protokollführung das Issue trotzdem schließen, mit Hinweis in der nächsten Sitzung. So bleibt der Prozess auch bei urlaubsbedingten Verzögerungen handlungsfähig.

</details>

## Verwandte Seiten

* [Thema vorschlagen](thema-vorschlagen.md)
* [Aufgabe erfassen](aufgabe-erfassen.md)
* [Sitzung durchführen](sitzung-durchfuehren.md)
* [Aufgaben-Board](aufgaben-board.md)
* [Issue-Typen und Labels](issue-typen-und-labels.md)
* [Häufige Fragen](haeufige-fragen.md)
* [Setup-Anleitung](../../docs/setup.md) – technische Einrichtung (für Admins)

## Seiten-Glossar

| Begriff | Definition |
|---|---|
| Action Item | Eine aus einem Beschluss entstandene Aufgabe mit verantwortlicher Person und Fälligkeit, geführt als eigenes Issue. |
| Board-Status | Spalte eines Issues im Aufgaben-Board; unabhängig vom Issue-Status (offen/geschlossen) auf GitHub. |

---

## Transport-Metadaten (beim Erfassen in Felder übertragen, dann diesen Block löschen)

* Seitentyp: Hintergrund/Konzept
* Verantwortliche Rolle: GitHub-Spezialist
* Themengebiet: Organisation
* Zielgruppe: Alle Mitglieder
* Eltern-Seite: Aufgaben und Sitzungsverwaltung
* Reihenfolge: 70
* Textauszug: Diese Seite erklärt, warum das Learn WP DACH Team Sitzungsplanung, Beschlussprotokolle und Aufgaben über GitHub Issues und ein Kanban Board verwaltet, und welche Grundkonzepte dabei gelten.
* Letzte Aktualisierung: 2026-07-12
* Letzte Prüfung: 2026-05-03
* Prüfintervall: 365
