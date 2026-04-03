# Benutzeranleitung: Sitzungsverwaltung auf GitHub

Diese Anleitung richtet sich an alle Teammitglieder des Learn WP DACH Teams.

---

## Inhaltsverzeichnis

- [Thema vorschlagen](#thema-vorschlagen)
- [Sitzungs-Issue verwalten (Moderation & Protokollführung)](#sitzungs-issue-verwalten-moderation--protokollführung)
- [Aufgabe erfassen](#aufgabe-erfassen)
- [Kanban Board nutzen](#kanban-board-nutzen)
- [Protokolle finden](#protokolle-finden)
- [Häufige Fragen](#häufige-fragen)

---

## Thema vorschlagen

Möchtest du ein Thema in die nächste Sitzung einbringen?

1. [Issues](https://github.com/rfluethi/learn-wp-dach-team/issues) → **New issue**
2. Vorlage **Thema** wählen
3. Ausfüllen:
   - **Titel:** Kurzer, prägnanter Thementitel
   - **Vorgeschlagen von:** Dein Name
   - **Art:** Information / Diskussion / Entscheidung
   - **Beschreibung:** Was ist das Thema?
   - **Gewünschtes Ergebnis:** Was soll am Ende feststehen?
4. Label `thema` setzen
5. Issue erstellen
6. Im [Aufgaben-Board](https://github.com/users/rfluethi/projects/11) das Issue öffnen und das Feld **Estimate** mit der geschätzten Anzahl Minuten ausfüllen

> Das Feld **Estimate** ermöglicht bei der Sitzungsplanung eine Übersicht über die voraussichtliche Gesamtdauer der Sitzung.

Der Moderator verlinkt dein Thema im Sitzungs-Issue unter Punkt 6.

---

## Sitzungs-Issue verwalten *(Moderation & Protokollführung)*

Der Prozess läuft in drei Schritten ab:

---

### Schritt 1: Issue erstellen *(Moderation, 1 Woche vor der Sitzung)*

1. [Issues](https://github.com/rfluethi/learn-wp-dach-team/issues) → **New issue**
2. Vorlage **Sitzung** wählen
3. Titel setzen: `Sitzung YYYY-MM-DD` (z.B. `Sitzung 2026-04-28`)
4. Felder ausfüllen: Datum, Uhrzeit, Moderation, Protokollführung
5. Issue erstellen → das ist die Themenliste

> Das Label `sitzung` wird durch die Vorlage automatisch gesetzt – kein manuelles Labeling nötig.

---

### Schritt 2: Sitzung vorbereiten *(Moderation, vor der Sitzung)*

1. Alle eingereichten Themen-Issues unter **Punkt 6 (Diskussionsthemen)** verlinken: `- [ ] #42`
2. Reihenfolge der Themen festlegen
3. **Board-Status** auf **In Arbeit** setzen: [Aufgaben-Board](https://github.com/users/rfluethi/projects/11) → Sitzungs-Issue anklicken → rechts im Panel **Status → In Arbeit** wählen

> **Hinweis:** Der Board-Status (im Aufgaben-Board) ist unabhängig vom GitHub-Issue-Status (offen/geschlossen). Hier wird immer der **Board-Status** gemeint.

---

### Schritt 3: Protokoll erstellen *(Protokollführung)*

**Während der Sitzung:**

- Beschlüsse direkt ins Issue eintragen (Abschnitt *Beschlüsse*)
- Kernaussagen pro Thema notieren (Abschnitt *Notizen*)

**Nach der Sitzung:**

1. Für jede beschlossene Aufgabe ein neues [Aufgaben-Issue erstellen](#aufgabe-erfassen)
2. Links zu den Aufgaben-Issues im Abschnitt *Aufgaben* eintragen: `- #23 @username`
3. Themen-Issues schliessen (erledigt) oder mit Label `nächste-sitzung` versehen (vertagt)
4. Themen-Issues, die zu einem formellen Entscheid geführt haben, zusätzlich mit Label `beschluss` versehen – so sind alle Beschlüsse über `label:beschluss` auffindbar
5. **Board-Status** auf **Blockiert** setzen → zeigt dem Team: Protokoll ist bereit zur Prüfung
6. Kommentar ins Issue schreiben: *"Protokoll ist fertig – bitte prüfen und mit OK bestätigen."*
7. Sobald mindestens ein OK-Kommentar eingegangen ist: Issue **schliessen** → wird automatisch ins Protokoll-Archiv aufgenommen

> Das geschlossene Issue ist das offizielle Beschlussprotokoll. Das Vier-Augen-Prinzip stellt sicher, dass das Protokoll von mindestens einem weiteren Teammitglied geprüft wurde.
>
> **Timeout:** Falls nach 3 Werktagen kein OK eingegangen ist, kann die Protokollführung das Issue auch ohne Kommentar schliessen und in der nächsten Sitzung kurz darauf hinweisen.

---

## Aufgabe erfassen

1. [Issues](https://github.com/rfluethi/learn-wp-dach-team/issues) → **New issue**
2. Vorlage **Aufgabe** wählen
3. Ausfüllen:
   - **Titel:** `Aufgabe: [kurze Beschreibung]`
   - **Verantwortlich:** GitHub-Username (z.B. `@rfluethi`)
   - **Fällig bis:** Datum im Format `YYYY-MM-DD`
   - **Herkunft:** Nummer des Sitzungs-Issues (z.B. `#42`)
   - **Abhängigkeiten:** Was muss vorher erledigt sein?
   - **Beschreibung:** Was genau muss gemacht werden?
   - **Erledigungskriterium:** Woran erkennen wir, dass es fertig ist?
4. Label `aufgabe` ist durch die Vorlage bereits gesetzt – kein manuelles Labeling nötig
5. Person zuweisen (Assignee)
6. Issue erstellen → erscheint automatisch im Kanban Board

---

## Kanban Board nutzen

Das [Aufgaben-Board](https://github.com/users/rfluethi/projects/11) zeigt alle offenen Aufgaben.

**Spalten:**

| Spalte | Bedeutung |
| --- | --- |
| Themen | Vorgeschlagene Themen für nächste Sitzung |
| Offen | Aufgabe noch nicht begonnen |
| In Arbeit | Aktiv in Bearbeitung / Sitzung in Vorbereitung |
| Blockiert | Aufgabe hat Blocker – oder: Protokoll wartet auf Review (OK) |
| Erledigt | Fertig |

**Vordefinierte Views:**

| View | Link | Zeigt |
| --- | --- | --- |
| My Items | [Meine Aufgaben](https://github.com/users/rfluethi/projects/11/views/5?sliceBy%5Bvalue%5D=In+Arbeit) | Nur eigene Aufgaben |
| Lerngruppe | [Lerngruppen-Aufgaben](https://github.com/users/rfluethi/projects/11/views/6) | Alle Aufgaben mit Label `lerngruppe` |
| Webseite | [Webseiten-Aufgaben](https://github.com/users/rfluethi/projects/11/views/7) | Alle Aufgaben mit Label `webseite` |
| Sitzungsvorbereitung | [Themen](https://github.com/users/rfluethi/projects/11/views/8?groupedBy%5BcolumnId%5D=Assignees&sliceBy%5BcolumnId%5D=Assignees) | Vorgeschlagene Diskussionsthemen |
| Protokolle | [Protokoll-Archiv](https://github.com/users/rfluethi/projects/11/views/10) | Alle geschlossenen Sitzungs-Issues |

**Weitere Tipps:**

- Issues per Drag & Drop zwischen Spalten verschieben
- Eigene Aufgaben: Filter `assignee:@me` im Suchfeld

> **Hinweis:** Die Links zu den Board-Views enthalten hardkodierte View-IDs. Nach einem Repository-Neuaufbau oder Transfer müssen diese Links in dieser Anleitung aktualisiert werden.

---

## Protokolle finden

**Alle Protokolle auf einen Blick:** → [README.md](https://github.com/rfluethi/learn-wp-dach-team/blob/main/README.md) (wird automatisch aktualisiert)

**Direktsuche:** Issues → Filter eingeben: `label:sitzung is:closed`

**Einzelnes Protokoll:** Issues → geschlossenes Sitzungs-Issue öffnen

---

## Häufige Fragen

**Kann ich ein Thema auch spontan in der Sitzung einbringen?**
Ja – der Moderator fügt es direkt in Punkt 6 des Sitzungs-Issues ein, ohne separates Issue.

**Was passiert mit vertagten Themen?**
Label `nächste-sitzung` setzen. Der Moderator der nächsten Sitzung verlinkt es dann.

**Wer kann Issues erstellen und bearbeiten?**
Alle eingeladenen Teammitglieder (Collaborators). GitHub-Account ist Voraussetzung.

**Wie finde ich meine offenen Aufgaben?**
Aufgaben-Board → Filter `assignee:@me` oder direkt: Issues → `is:open label:aufgabe assignee:@me`

**Ein Sitzungs-Issue ist versehentlich im Kanban gelandet – was tun?**
Issue aus dem Board entfernen: Board → Issue → drei Punkte → *Remove from project*
