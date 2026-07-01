# Sitzung durchführen: vom Issue zum Protokoll

## Kurzbeschreibung

Beschreibt den Prozess von der Sitzungsvorbereitung bis zum geschlossenen Beschlussprotokoll. Diese Seite richtet sich an die Rollen **Moderation** und **Protokollführung**.

## Auslöser

Eine Woche vor dem nächsten Sitzungstermin.

## Beteiligte Rollen

* **Moderation:** erstellt das Sitzungs-Issue, sammelt Themen, leitet die Sitzung
* **Protokollführung:** dokumentiert Beschlüsse und Aufgaben, führt das Issue zum Abschluss
* **Team:** prüft das fertige Protokoll und bestätigt mit OK

## Ablauf

### 1. Issue erstellen *(Moderation, eine Woche vor der Sitzung)*

1. Die Moderation öffnet die [Issues-Übersicht](https://github.com/rfluethi/learn-wp-dach-team/issues) und klickt auf **New issue**.
2. Sie wählt die Vorlage **Sitzung**.
3. Sie setzt den Titel im Format `Sitzung JJJJ-MM-TT` (z.B. `Sitzung 2026-04-28`).
4. Sie füllt die Felder aus: Datum, Uhrzeit, Moderation, Protokollführung.
5. Sie erstellt das Issue. Damit ist die Themenliste angelegt.

<details>
<summary>Hinweis zum Label „sitzung"</summary>

Die Vorlage **Sitzung** setzt das Label `sitzung` automatisch. Manuelles Labeling ist nicht nötig.

</details>

### 2. Sitzung vorbereiten *(Moderation, vor der Sitzung)*

1. Die Moderation verlinkt alle eingereichten Themen-Issues unter **Punkt 6 (Diskussionsthemen)** des Sitzungs-Issues: `- [ ] #42`.
2. Sie legt die Reihenfolge der Themen fest.
3. Sie setzt den Board-Status des Sitzungs-Issues auf **In Arbeit**: [Aufgaben-Board](https://github.com/users/rfluethi/projects/11) öffnen → Sitzungs-Issue anklicken → im Panel rechts **Status → In Arbeit** wählen.

<details>
<summary>Board-Status vs. Issue-Status</summary>

Der Board-Status (im Aufgaben-Board) ist unabhängig vom GitHub-Issue-Status (offen/geschlossen). In dieser Anleitung ist immer der **Board-Status** gemeint.

</details>

### 3. Beschlüsse und Notizen erfassen *(Protokollführung, während der Sitzung)*

1. Die Protokollführung trägt Beschlüsse direkt im Sitzungs-Issue ein, im Abschnitt *Beschlüsse*.
2. Sie notiert Kernaussagen pro Thema im Abschnitt *Notizen*.

### 4. Aufgaben anlegen *(Protokollführung, nach der Sitzung)*

1. Für jede beschlossene Aufgabe legt die Protokollführung ein neues Aufgaben-Issue an. Siehe [Aufgabe erfassen](aufgabe-erfassen.md).
2. Sie verlinkt die Aufgaben-Issues im Abschnitt *Aufgaben* des Sitzungs-Issues: `- #23 @username`.

### 5. Themen-Issues abschliessen *(Protokollführung)*

1. Die Protokollführung schliesst erledigte Themen-Issues.
2. Vertagte Themen erhalten das Label `nächste-sitzung`.
3. Themen-Issues, die zu einem formellen Entscheid geführt haben, erhalten zusätzlich das Label `beschluss`.

<details>
<summary>Wozu das Label „beschluss"?</summary>

Über die Suche `label:beschluss` sind alle Beschlüsse auf einen Blick auffindbar, unabhängig davon, in welcher Sitzung sie gefasst wurden.

</details>

### 6. Protokoll zur Prüfung freigeben *(Protokollführung)*

1. Die Protokollführung setzt den Board-Status des Sitzungs-Issues auf **Blockiert**. Das signalisiert dem Team: Protokoll ist bereit zur Prüfung.
2. Sie schreibt einen Kommentar ins Issue: *„Protokoll ist fertig – bitte prüfen und mit OK bestätigen."*

### 7. Protokoll abschliessen *(Protokollführung, nach Bestätigung)*

1. Sobald mindestens ein OK-Kommentar eingegangen ist, schliesst die Protokollführung das Issue.
2. Das geschlossene Issue erscheint automatisch im [Protokoll-Archiv](https://github.com/users/rfluethi/projects/11/views/10).

<details>
<summary>Vier-Augen-Prinzip und Timeout</summary>

Das geschlossene Issue ist das offizielle Beschlussprotokoll. Das OK-Kommentar stellt sicher, dass mindestens ein weiteres Teammitglied das Protokoll geprüft hat.

Falls nach drei Werktagen kein OK eingegangen ist, kann die Protokollführung das Issue auch ohne Kommentar schliessen und in der nächsten Sitzung kurz darauf hinweisen.

</details>

## Ergebnis

Das Sitzungs-Issue ist geschlossen, alle Aufgaben sind als eigene Issues erfasst, und das Protokoll ist im Archiv auffindbar.

## Verwandte Seiten

* [Thema vorschlagen](thema-vorschlagen.md) – wie Themen in die Sitzung kommen
* [Aufgabe erfassen](aufgabe-erfassen.md) – Detail zu Schritt 4
* [Aufgaben-Board](aufgaben-board.md) – wie der Board-Status funktioniert
* [Häufige Fragen](haeufige-fragen.md) – Sonderfälle (spontane Themen, vertagte Themen)
* [GitHub-basierte Sitzungsverwaltung](WordPress-Training-Team-DACH/GitHub-Repo/learn-wp-dach-team/handbuch/Aufgaben%20und%20Sitzungsverwaltung/konzept.md) – Hintergrund zum Workflow

## Metadaten

*Verantwortliche Rolle: GitHub-Spezialist · Letzte Aktualisierung: 2026-05-03 · Letzte Prüfung: 2026-05-03*
