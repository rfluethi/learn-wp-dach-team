# Leitprinzipien des Handbuchs

## Kurzbeschreibung

Diese Seite beantwortet die Frage: **Nach welchen Grundsätzen erstellen wir Handbuch-Inhalte und warum?** Sie richtet sich an alle Personen, die am Handbuch mitwirken.

## Worum geht es

Das Handbuch hat zwei Zielgruppen mit konkurrierenden Bedürfnissen, und es gibt neun Leitprinzipien, mit denen wir beide Gruppen mit *einem* Dokument bedienen.

## Zwei Zielgruppen, ein Dokument

Das Handbuch hat zwei Zielgruppen mit konkurrierenden Bedürfnissen:

| Zielgruppe | Bedürfnis | Was sie brauchen |
|---|---|---|
| **Neue Teammitglieder** (Onboarding) | Lernen, Verstehen, Kontext aufbauen | Einordnung, „Warum machen wir das?", Beispiele, mehr Hintergrund |
| **Bestehende Teammitglieder** (Nachschlagen) | Schnell finden, schnell erledigen | Knappe Schritte, klare Struktur, kein Ballast |

### Unsere Lösung

Wir erstellen **kein zweites Handbuch** für Neueinsteiger. Doppelte Pflege führt erfahrungsgemäß zu Versionsabweichungen und Mehraufwand.

Stattdessen kombinieren wir zwei etablierte Ansätze:

1. **Inhaltstypen klar trennen** ([Diátaxis-Framework](https://diataxis.fr/)). Eine Seite hat **einen** Hauptzweck, entweder Anleitung, Erklärung oder Nachschlagewerk. Mischformen vermeiden wir.
2. **Progressive Disclosure** ([Nielsen Norman Group, 1995](https://www.nngroup.com/articles/progressive-disclosure/)). Kontextinformationen für Neueinsteiger platzieren wir in Aufklappbereichen mit Titeln nach dem Muster „Kategorie: worum es geht" (z.B. „Hintergrund: Wozu Labels dienen"). Wer schnell nachschlagen will, sieht sie nicht. Wer lernen will, klappt sie auf.

Wie wir das praktisch umsetzen, steht in [Inhaltstypen und Vorlagen](inhaltstypen-und-vorlagen.md).

## Warum machen wir das so

Die folgenden neun Prinzipien gelten für jede Seite des Handbuchs.

**P1, Eine Seite, ein Hauptzweck.**
Jede Seite ist primär entweder Anleitung, Erklärung oder Nachschlagewerk, nie alles gleichzeitig. Mischformen verwirren beide Zielgruppen. Siehe [Diátaxis-Framework](https://diataxis.fr/start-here/).

**P2, Nicht duplizieren, verlinken.**
Externe Tool-Dokumentationen (Hersteller, offizielle Quellen) verlinken wir, kopieren wir nicht. Wir dokumentieren nur, was unsere Gruppe spezifisch betrifft. Details in [Schreibregeln und Markdown-Konventionen](schreibregeln-und-markdown.md).

**P3, Progressive Disclosure.**
Pflichtinformationen stehen oben und sichtbar. Hintergrund, Begründungen und Detailwissen für Neueinsteiger gehören in Aufklappbereiche mit Titeln nach dem Muster „Kategorie: worum es geht".

**P4, Aktion vor Theorie.**
Bei Anleitungen kommt zuerst, **was zu tun ist**. Das **Warum** folgt, falls nötig, im Aufklappbereich.

**P5, Single Source of Truth.**
Jede Information existiert an genau **einer** Stelle im Handbuch. Andere Stellen verlinken dorthin. So bleibt das Handbuch pflegbar.

**P6, Aktualität sichtbar machen.**
Jede Seite zeigt, wann wir sie zuletzt aktualisiert und zuletzt geprüft haben, sowie welche Rolle dafür verantwortlich ist. Diese Angaben leben in WordPress **als Felder**; die Fußzeile rendert sie automatisch. In Markdown-Entwürfen reisen sie im Transport-Block mit.

**P7, Verantwortlichkeiten über Rollen, nicht über Personen.**
Wir weisen Verantwortlichkeiten im Handbuch ausschließlich über **Rollen** zu, nicht über konkrete Personen. So müssen wir bei einem personellen Wechsel nicht das ganze Handbuch überarbeiten. Die Zuordnung Person zu Rolle pflegen wir an einer einzigen, zentralen Stelle.

**P8, Nutzerperspektive vor Tool-Logik.**
Anleitungen organisieren wir nach **Aufgaben** („So buchst du eine Reise"), nicht nach **Tool-Menüpunkten**. Das gilt insbesondere für [How-to-Guides](https://diataxis.fr/how-to-guides/).

**P9, Handbook-first-Kultur.**
Ändert sich ein Prozess oder ein Tool, aktualisieren wir die betroffene Seite im selben Arbeitsgang. Das Handbuch läuft der Realität nicht hinterher.

## Was bedeutet das für unsere Arbeit

Die Prinzipien sind keine theoretische Übung, sondern bilden die Basis aller anderen Regelwerk-Seiten. Konkret:

* P1 ist die Grundlage der Seitentypen — siehe [Inhaltstypen und Vorlagen](inhaltstypen-und-vorlagen.md).
* P2 prägt unseren Umgang mit externen Dokumentationen — siehe [Schreibregeln und Markdown-Konventionen](schreibregeln-und-markdown.md).
* P3 und P4 bestimmen den Aufbau jeder Seite — siehe [Inhaltstypen und Vorlagen](inhaltstypen-und-vorlagen.md).
* P5 erklärt, warum Vorlagen und Review-Checkliste nur an einem Ort liegen — siehe [Erstellungs- und Pflegeprozess](erstellungs-und-pflegeprozess.md).
* P6 ist die Grundlage der Metadaten-Felder und des Transport-Blocks.
* P7 prägt den [Erstellungs- und Pflegeprozess](erstellungs-und-pflegeprozess.md).
* P8 ist die Grundregel beim Schreiben von Anleitungen.
* P9 hält das Handbuch aktuell — siehe [Erstellungs- und Pflegeprozess](erstellungs-und-pflegeprozess.md).

## Verwandte Seiten

* [Regelwerk-Übersicht](README.md)
* [Inhaltstypen und Vorlagen](inhaltstypen-und-vorlagen.md)
* [Schreibregeln und Markdown-Konventionen](schreibregeln-und-markdown.md)
* [Erstellungs- und Pflegeprozess](erstellungs-und-pflegeprozess.md)

## Seiten-Glossar

| Begriff | Definition |
|---|---|
| Aufklappbereich | HTML-`<details>`-Element für ergänzende Informationen, mit kurzem, beschreibendem Titel (z.B. „Hintergrund"). |
| Rolle | Funktionsbezeichnung im Team, der Verantwortlichkeiten zugeordnet sind (nicht eine konkrete Person). |
| Transport-Block | Block am Ende jedes Markdown-Entwurfs, der die Metadaten zur Erfassung transportiert; wird beim Import in WordPress-Felder übertragen und aus dem Inhalt gelöscht. |

## Transport-Metadaten (beim Erfassen in Felder übertragen, dann diesen Block löschen)

* Seitentyp: Hintergrund/Konzept
* Verantwortliche Rolle: GitHub-Spezialist
* Themengebiet: Organisation
* Zielgruppe: Inhalts-Ersteller:innen
* Eltern-Seite: Handbuch-Erstellung
* Reihenfolge: 10
* Textauszug: Diese Seite beantwortet die Frage: Nach welchen Grundsätzen erstellen wir Handbuch-Inhalte und warum?
* Letzte Aktualisierung: 2026-07-12
* Letzte Prüfung: 2026-05-03
* Prüfintervall: 365
