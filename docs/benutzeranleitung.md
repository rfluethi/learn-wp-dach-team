# Benutzeranleitung: Sitzungsverwaltung auf GitHub

Diese Anleitung richtet sich an alle Teammitglieder des Learn WP DACH Teams.

---

## Inhaltsverzeichnis

- [Traktandum vorschlagen](#traktandum-vorschlagen)
- [Sitzungs-Issue erstellen (Moderation)](#sitzungs-issue-erstellen-moderation)
- [Protokoll ausfüllen (Protokollführung)](#protokoll-ausfüllen-protokollführung)
- [Aufgabe erfassen](#aufgabe-erfassen)
- [Kanban Board nutzen](#kanban-board-nutzen)
- [Protokolle finden](#protokolle-finden)
- [Häufige Fragen](#häufige-fragen)

---

## Traktandum vorschlagen

Möchtest du ein Thema in die nächste Sitzung einbringen?

1. [Issues](../../issues) → **New issue**
2. Vorlage **Traktandum** wählen
3. Ausfüllen:
   - **Titel:** Kurzer, prägnanter Thementitel
   - **Vorgeschlagen von:** Dein Name
   - **Art:** Information / Diskussion / Entscheidung
   - **Zeitbedarf:** Geschätzte Minuten
   - **Beschreibung:** Was ist das Thema?
   - **Gewünschtes Ergebnis:** Was soll am Ende feststehen?
4. Label `traktandum` setzen
5. Issue erstellen

Der Moderator verlinkt dein Traktandum im Sitzungs-Issue unter Punkt 6.

---

## Sitzungs-Issue erstellen *(Moderation)*

**Wann:** 1 Woche vor der Sitzung

1. [Issues](../../issues) → **New issue**
2. Vorlage **Sitzung** wählen
3. Titel setzen: `Sitzung YYYY-MM-DD` (z.B. `Sitzung 2026-04-28`)
4. Felder ausfüllen: Datum, Uhrzeit, Moderation, Protokollführung
5. Issue erstellen → das ist die Traktandenliste

**Vor der Sitzung:**
- Alle eingereichten Traktanden-Issues unter Punkt 6 verlinken: `- [ ] #42`
- Reihenfolge festlegen
- Link zum [Aufgaben-Board](../../projects/1) unter Punkt 3 eintragen

---

## Protokoll ausfüllen *(Protokollführung)*

**Zuständigkeit:** Rotierend – wer dran ist, steht im Sitzungs-Issue.

**Während der Sitzung:**
- Beschlüsse direkt ins Issue eintragen (Abschnitt *Beschlüsse*)
- Kernaussagen pro Thema notieren (Abschnitt *Notizen*)

**Nach der Sitzung:**
1. Für jede beschlossene Aufgabe ein neues [Aufgaben-Issue erstellen](#aufgabe-erfassen)
2. Links zu den Aufgaben-Issues im Abschnitt *Aufgaben* eintragen: `- #23 @username`
3. Traktanden-Issues schliessen (erledigt) oder mit Label `nächste-sitzung` versehen (vertagt)
4. Sitzungs-Issue **schliessen** → wird automatisch ins Protokoll-Archiv aufgenommen

> Das geschlossene Issue ist das offizielle Beschlussprotokoll.

---

## Aufgabe erfassen

1. [Issues](../../issues) → **New issue**
2. Vorlage **Aufgabe** wählen
3. Ausfüllen:
   - **Titel:** `Aufgabe: [kurze Beschreibung]`
   - **Verantwortlich:** GitHub-Username (z.B. `@rfluethi`)
   - **Fällig bis:** Datum im Format `YYYY-MM-DD`
   - **Herkunft:** Nummer des Sitzungs-Issues (z.B. `#42`)
   - **Abhängigkeiten:** Was muss vorher erledigt sein?
   - **Beschreibung:** Was genau muss gemacht werden?
   - **Erledigungskriterium:** Woran erkennen wir, dass es fertig ist?
4. Label `aufgabe` setzen
5. Person zuweisen (Assignee)
6. Issue erstellen → erscheint automatisch im Kanban Board

---

## Kanban Board nutzen

Das [Aufgaben-Board](../../projects/1) zeigt alle offenen Aufgaben.

**Spalten:**

| Spalte | Bedeutung |
|---|---|
| Traktanden | Vorgeschlagene Themen für nächste Sitzung |
| Offen | Aufgabe noch nicht begonnen |
| In Arbeit | Aktiv in Bearbeitung |
| Blockiert | Warte auf etwas – Abhängigkeit im Issue beschreiben |
| Erledigt | Fertig |

**Tipps:**
- Issues per Drag & Drop zwischen Spalten verschieben
- Eigene Aufgaben anzeigen: Filter `assignee:@me`
- Nur Lerngruppen-Themen: Filter `label:lerngruppe`

---

## Protokolle finden

**Alle Protokolle auf einen Blick:** → [README.md](../../blob/main/README.md) (wird automatisch aktualisiert)

**Direktsuche:** Issues → Filter eingeben: `label:sitzung is:closed`

**Einzelnes Protokoll:** Issues → geschlossenes Sitzungs-Issue öffnen

---

## Häufige Fragen

**Kann ich ein Traktandum auch spontan in der Sitzung einbringen?**
Ja – der Moderator fügt es direkt in Punkt 6 des Sitzungs-Issues ein, ohne separates Issue.

**Was passiert mit vertagten Traktanden?**
Label `nächste-sitzung` setzen. Der Moderator der nächsten Sitzung verlinkt es dann.

**Wer kann Issues erstellen und bearbeiten?**
Alle eingeladenen Teammitglieder (Collaborators). GitHub-Account ist Voraussetzung.

**Wie finde ich meine offenen Aufgaben?**
Aufgaben-Board → Filter `assignee:@me` oder direkt: Issues → `is:open label:aufgabe assignee:@me`

**Ein Sitzungs-Issue ist versehentlich im Kanban gelandet – was tun?**
Issue aus dem Board entfernen: Board → Issue → drei Punkte → *Remove from project*
