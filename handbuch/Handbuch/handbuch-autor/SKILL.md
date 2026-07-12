---
name: handbuch-autor
description: Erstellt, prüft, überarbeitet und teilt Inhalte für unser Team-Handbuch auf und bereitet sie für die Erfassung in WordPress vor. Setze diesen Skill IMMER ein, wenn der Mensch eine Handbuch-Seite schreiben, überarbeiten, prüfen, strukturieren, aufteilen oder in WordPress erfassen will, oder wenn von "Anleitung", "How-to", "Prozessbeschreibung", "Tool-Übersicht", "Rollenbeschreibung", "FAQ" oder "Hintergrundseite" für das interne Handbuch die Rede ist. Nutze ihn auch, wenn der Mensch nur sagt "ich muss noch was fürs Handbuch schreiben", "kannst du das fürs Wiki dokumentieren" oder "diese Seite ist ein Mischmasch, kannst du sie aufräumen", ohne den Seitentyp explizit zu nennen. Der Skill stellt sicher, dass jede Seite der Anleitung zur Erstellung des Team-Handbuchs folgt: ein Hauptzweck pro Seite (Diátaxis), Progressive Disclosure mit dem Standard-Aufklappbereich "Für neue Mitglieder", Verlinkung statt Duplizierung, Verantwortung über Rollen, Metadaten als Transport-Block (in WordPress als Felder), amtliche deutsche Rechtschreibung mit ß und konsistente Markdown-Struktur für die WordPress-Veröffentlichung.
---

# Skill: handbuch-autor

Dieser Skill unterstützt beim Erstellen, Prüfen, Überarbeiten, **Aufteilen** und **Erfassen** von Seiten für unser Team-Handbuch. Er setzt die *Anleitung zur Erstellung des Team-Handbuchs* (Version 1.4) um. Bei Widersprüchen gilt die Anleitung.

## Wann triggern

Setze diesen Skill ein, sobald jemand:

* eine **neue Seite** für das Handbuch schreiben will,
* eine **bestehende Seite überarbeiten** möchte,
* eine Seite **reviewen** oder gegen die Qualitätskriterien prüfen will,
* einen **bestehenden, gemischten Inhalt aufteilen** will (z.B. eine alte Wiki-Seite, die mehrere Themen vermischt),
* eine fertige Seite **in WordPress erfassen** will,
* unsicher ist, ob ein Inhalt überhaupt ins Handbuch gehört oder wie er strukturiert werden soll,
* allgemein über „Doku", „Anleitung", „Prozess dokumentieren", „Wiki-Eintrag", „aufräumen" oder „fürs Handbuch" spricht.

## Grundsätze, die dieser Skill konsequent umsetzt

Diese Grundsätze stammen aus der Anleitung (Kapitel 3). Halte dich an sie auch dann, wenn der Mensch sie nicht nennt.

* **P1, ein Hauptzweck pro Seite** ([Diátaxis-Framework](https://diataxis.fr/)). Eine Seite ist Anleitung **oder** Erklärung **oder** Nachschlagewerk, nicht alles gleichzeitig.
* **P2, nicht duplizieren, verlinken.** Hersteller-Dokumentationen werden verlinkt, nie kopiert.
* **P3, Progressive Disclosure.** Pflichtinformationen sichtbar; Hintergrund in Aufklappbereichen, Kontext für Neueinsteiger im Standard-Aufklappbereich **„Für neue Mitglieder"** (fester Titel).
* **P4, Aktion vor Theorie.** Bei Anleitungen kommt zuerst, was zu tun ist.
* **P5, Single Source of Truth.** Jede Information existiert genau einmal; andere Stellen verlinken. Einzige Ausnahme: wortgleiche Glossar-Definitionen auf mehreren Seiten.
* **P6, Aktualität sichtbar machen.** Verantwortliche Rolle, letzte Aktualisierung und letzte Prüfung werden in WordPress **als Felder** gepflegt und vom Template angezeigt. In Markdown-Entwürfen reisen sie im Transport-Block mit (siehe `references/markdown-konventionen.md`).
* **P7, Rollen statt Personen.** Verantwortlichkeit über Rollen; Urheberschaft (wer schrieb, wer prüfte) ist davon getrennt und personengebunden.
* **P8, Nutzerperspektive vor Tool-Logik.** Anleitungen sind nach Aufgaben strukturiert, nicht nach Tool-Menüs.
* **P9, Handbook-first-Kultur.** Ändert sich ein Prozess oder Tool, wird die betroffene Seite im selben Arbeitsgang aktualisiert.

## Arbeitsmodus: zwei Wege je nach Bedarf

### Modus A, beratend („KI fragt, schlägt vor, Mensch entscheidet")

Nutze diesen Modus, wenn das Thema fachlich komplex ist, die Seite organisatorische Festlegungen enthält (Rollen, Befugnisse), der Mensch Unsicherheit signalisiert, oder eine **Aufteilung** ansteht (immer beratend, weil Strukturentscheidung).

Vorgehen: Stelle gezielte Fragen (Frageleitfaden der jeweiligen Vorlage), formuliere Strukturvorschläge, lass den Menschen entscheiden, schreibe dann den Entwurf.

### Modus B, generierend („KI erstellt direkt einen Entwurf")

Nutze diesen Modus, wenn der Mensch eine klare Aufgabe beschreibt, die nötigen Informationen bereits vorliegen oder er ausdrücklich um einen direkten Entwurf bittet.

Vorgehen: Erstelle direkt einen vollständigen Markdown-Entwurf nach der passenden Vorlage. Markiere alle Annahmen mit `[ANNAHME: …]`.

**Nicht raten bei:** verantwortlichen Rollen, internen Tool-Konventionen, organisatorischen Abläufen, Eltern-Seite und Reihenfolge im Menü. Diese kommen vom Menschen oder bleiben Platzhalter `[Rolle]`, `[wird ergänzt]`.

## Die fünf Workflows im Überblick

| Workflow | Wann einsetzen |
|---|---|
| W1, neue Seite | Es gibt noch keinen Inhalt; eine Seite soll von Grund auf entstehen. |
| W2, bestehende Seite überarbeiten | Inhalt existiert, Seitentyp ist eindeutig, nur die Form soll verbessert werden. |
| W3, bestehenden Inhalt aufteilen | Inhalt existiert, vermischt aber mehrere Seitentypen oder Themen. |
| W4, Review | Nur prüfen, nicht ändern. Befunde melden. |
| W5, WordPress-Erfassung | Ein fertiger Entwurf soll in WordPress eingepflegt werden. |

**Wichtig:** Bei einer Überarbeitungsanfrage (W2) prüfst du immer **zuerst**, ob in Wahrheit W3 nötig ist. Diese Entscheidung trifft `references/aufteilen.md`.

## W1, neue Seite

Folge diesen Schritten in dieser Reihenfolge. Überspringe keinen.

1. **Seitentyp bestimmen.** Lade `references/inhaltstypen.md`. Passen mehrere Typen, ist es vermutlich eine Mischform: nachfragen.
2. **Passende Vorlage laden.** Nur die eine passende Datei:

   | Seitentyp | Referenzdatei |
   |---|---|
   | Anleitung (How-to) | `references/vorlage-anleitung.md` |
   | Prozessbeschreibung | `references/vorlage-prozess.md` |
   | Tool-Übersicht | `references/vorlage-tool.md` |
   | Rollen-/Organisationsbeschreibung | `references/vorlage-rolle.md` |
   | Hintergrund/Konzept | `references/vorlage-konzept.md` |
   | FAQ | `references/vorlage-faq.md` |

3. **Inhalte sammeln** (Modus A) oder **direkt entwerfen** (Modus B) nach dem Frageleitfaden der Vorlage. Frage dabei immer aktiv: **„Welche Begriffe dieser Seite brauchen einen Glossar-Eintrag?"** Das Seiten-Glossar steht am Ende vor dem Transport-Block; es leer zu lassen ist erlaubt, es zu vergessen nicht.
4. **Schreibregeln anwenden.** Lade `references/schreibregeln.md`.
5. **Markdown-Konventionen prüfen.** Lade `references/markdown-konventionen.md` (inkl. Dateiname = Slug und Transport-Block).
6. **Selbst-Check.** Lade `references/review-checkliste.md` und prüfe systematisch.
7. **Übergabe.** Liefere den Entwurf und nenne: den gewählten Seitentyp, alle `[ANNAHME: …]`-Stellen, alle Platzhalter, jede bewusste Abweichung von der Vorlage. Biete an, mit **W5** die WordPress-Erfassung zu begleiten.

## W2, bestehende Seite überarbeiten

1. **Vollständig lesen**, bevor du etwas tust.
2. **Mischform-Check (kritisch).** Lade `references/aufteilen.md`. Mischform erkannt: wechsle zu W3, bevor du irgendetwas umschreibst.
3. **Seitentyp bestätigen** (`references/inhaltstypen.md`).
4. **Vorlage laden und vergleichen.** Abweichungen auflisten.
5. **Schreibregeln und Markdown-Konventionen anwenden.**
6. **Übergabe mit Änderungsliste**: überarbeitete Fassung plus kurze Liste der Änderungen mit Begründung, damit der Mensch einzelne Änderungen ablehnen kann.

## W3, bestehenden Inhalt aufteilen

Aufteilen ist immer **Modus A** (beratend). Die Strukturentscheidung trifft der Mensch.

1. Inhalt vollständig lesen.
2. `references/aufteilen.md` laden und der Methode folgen (Symptome, absatzweise Klassifikation, Cluster, Seitenstruktur).
3. Aufteilungs-Vorschlag präsentieren: erkannte Symptome, neue Seiten mit Typ, Verlinkung, wegfallende Inhalte, Alternative (z.B. nur Aufklappbereiche).
4. **Bestätigung abwarten.** Tue nichts, bevor der Mensch entschieden hat.
5. Aufteilung ausführen: pro neuer Seite ein Entwurf nach Vorlage, Verlinkungs-Übersicht, Liste der Quellabsätze.
6. Fragen, ob die neuen Seiten direkt nach W2 überarbeitet werden sollen oder der Mensch das selbst tut.

## W4, Review

1. Seitentyp bestimmen.
2. Mischform prüfen (`references/aufteilen.md`); Befund festhalten.
3. `references/review-checkliste.md` Punkt für Punkt durchgehen.
4. Konkrete Funde mit Stellenverweis liefern (Format in der Checkliste).
5. Verbesserungen vorschlagen, **nicht ungefragt umschreiben**.

## W5, WordPress-Erfassung

Wenn ein Entwurf fertig ist und in WordPress eingepflegt werden soll: Lade `references/wordpress-erfassung.md` und führe den Menschen durch die Erfassung (Slug = Dateiname, Inhalt übertragen, Details-Blöcke, Seiten-Attribute für das Menü, Schlagworte, Textauszug, Metadaten-Felder, Transport-Block löschen, interne `.md`-Links auf die WordPress-Seiten umstellen).

## Was dieser Skill bewusst nicht tut

* Er **schreibt keine Hersteller-Dokumentationen ab** (P2); er verlinkt sie.
* Er **erfindet keine Rollennamen, Verantwortlichkeiten, Eltern-Seiten oder Menü-Reihenfolgen**. Unbekanntes wird als Platzhalter markiert.
* Er **setzt keine Datumsangaben**, die er nicht kennt (`[JJJJ-MM-TT]`).
* Er **teilt nicht ungefragt auf** und **verwendet keine Mischformen**. Lieber zwei kurze Seiten als eine vermischte.
* Er **schreibt Metadaten nie als dauerhaften Seiteninhalt**. Im Markdown-Entwurf reisen sie im Transport-Block mit; in WordPress leben sie ausschließlich in Feldern.

## Quellen, auf denen dieser Skill basiert

* Anleitung zur Erstellung des Team-Handbuchs (intern), Version 1.4. **Bei Widersprüchen gilt die Anleitung.**
* [Diátaxis-Framework](https://diataxis.fr/) für die Inhaltstypen.
* [Progressive Disclosure (Nielsen Norman Group)](https://www.nngroup.com/articles/progressive-disclosure/) für die Doppel-Zielgruppe.
* [tekom-Leitlinie „Regelbasiertes Schreiben"](https://www.tekom.de/fileadmin/tekom.de/Die_tekom/Publikationen/Leseproben/2013_RBS_Deutsch_fuer_die_TK_Leseprobe.pdf) für die Schreibregeln.
* Normen-Abgleich mit begründeten Abweichungen: siehe `../standards-abgleich.md` (nicht zur Laufzeit laden, Hintergrunddokument).
