# Aufgaben-Board

## Kurzbeschreibung

Das Aufgaben-Board ist das Kanban Board, in dem alle offenen Aufgaben und Diskussionsthemen verwaltet werden. Diese Seite ist eine Übersicht für alle Teammitglieder.

<details>
<summary>Hintergrund: Was ein Kanban Board ist</summary>

Ein Kanban Board zeigt Aufgaben als Karten in Spalten; jede Spalte ist ein Bearbeitungsstand, und Karten wandern von links (Offen) nach rechts (Erledigt). Warum wir Aufgaben so verwalten, erklärt die [Konzeptseite](konzept.md); die Bedienung von GitHub Projects beschreibt die [offizielle Dokumentation](https://docs.github.com/en/issues/planning-and-tracking-with-projects).

</details>

## Wer nutzt es

Alle Teammitglieder. Jedes Mitglied kann eigene Aufgaben einsehen, Themen einreichen und Aufgaben zwischen Spalten verschieben (sofern Mitwirkenden-Rechte bestehen).

## Zugang

Das Board ist öffentlich lesbar unter [Learn WP DACH – Aufgaben](https://github.com/users/rfluethi/projects/11). Schreibrechte (Aufgaben verschieben, Labels setzen) erhalten eingeladene Teammitglieder als Collaborators.

## Spalten

| Spalte | Bedeutung |
|---|---|
| Themen | Vorgeschlagene Themen für die nächste Sitzung |
| Offen | Aufgabe noch nicht begonnen |
| In Arbeit | Aktiv in Bearbeitung; Sitzung in Vorbereitung |
| Blockiert | Aufgabe hat Blocker oder Abhängigkeit |
| Überprüfung | Aufgabe erledigt, wartet auf Kontrolle durch eine zweite Person |
| Erledigt | Fertig und geprüft |

## Vordefinierte Views

| View | Link | Inhalt |
|---|---|---|
| My Items | [Meine Aufgaben](https://github.com/users/rfluethi/projects/11/views/5?sliceBy%5Bvalue%5D=In+Arbeit) | Nur eigene Aufgaben |
| Lerngruppe | [Lerngruppen-Aufgaben](https://github.com/users/rfluethi/projects/11/views/6) | Alle Aufgaben mit Label `lerngruppe` |
| Webseite | [Webseiten-Aufgaben](https://github.com/users/rfluethi/projects/11/views/7) | Alle Aufgaben mit Label `webseite` |
| Sitzungsvorbereitung | [Themen](https://github.com/users/rfluethi/projects/11/views/8?groupedBy%5BcolumnId%5D=Assignees&sliceBy%5BcolumnId%5D=Assignees) | Vorgeschlagene Diskussionsthemen |
| Protokolle | [Protokoll-Archiv](https://github.com/users/rfluethi/projects/11/views/10) | Alle geschlossenen Sitzungs-Issues |

## Unsere Konventionen

* Sitzungs-Issues erscheinen **nicht** im Board als reguläre Aufgaben. Sie sind über die View *Protokolle* auffindbar.
* Aufgaben werden per Drag-and-Drop zwischen Spalten verschoben.
* Eigene Aufgaben filtern: `assignee:@me` im Suchfeld eingeben.
* Landet ein Sitzungs-Issue versehentlich als reguläre Aufgabe im Board: Issue im Board öffnen und über das Drei-Punkte-Menü *Remove from project* entfernen. Das Issue selbst bleibt erhalten, nur die Board-Zuordnung wird entfernt.

## Offizielle Dokumentation

* [GitHub Projects: Documentation](https://docs.github.com/en/issues/planning-and-tracking-with-projects)

## Anleitungen mit diesem Tool

* [Thema vorschlagen](thema-vorschlagen.md)
* [Aufgabe erfassen](aufgabe-erfassen.md)
* [Sitzung durchführen](sitzung-durchfuehren.md)

<details>
<summary>Hinweis: Wartung der View-Links</summary>

Die Links zu den Board-Views enthalten hardkodierte View-IDs. Nach einem Repository-Neuaufbau oder Transfer müssen diese Links aktualisiert werden. Diese Pflege ist Teil der Setup-Anleitung; verantwortlich ist die Rolle, die auch das Repository administriert.

</details>

## Seiten-Glossar

| Begriff | Definition |
|---|---|
| Collaborator | Person mit Schreibrechten im Repository und Board, von der Repository-Administration eingeladen. |
| View | Gespeicherte Ansicht des Boards mit festen Filtern und Gruppierungen. |

---

## Transport-Metadaten (beim Erfassen in Felder übertragen, dann diesen Block löschen)

* Seitentyp: Tool-Übersicht
* Verantwortliche Rolle: GitHub-Spezialist
* Themengebiet: Organisation
* Zielgruppe: Alle Mitglieder
* Eltern-Seite: Aufgaben und Sitzungsverwaltung
* Reihenfolge: 40
* Textauszug: Das Aufgaben-Board ist das Kanban Board, in dem alle offenen Aufgaben und Diskussionsthemen verwaltet werden.
* Letzte Aktualisierung: 2026-07-12
* Letzte Prüfung: 2026-05-03
* Prüfintervall: 90
