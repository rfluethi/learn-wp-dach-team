## Kurzbeschreibung

Diese Seite beschreibt, wie eine Handbuch-Seite vom Bedarf bis zur Veröffentlichung entsteht und wie sie danach gepflegt wird. Sie enthält außerdem die Review-Checkliste für Selbst-Check und Peer-Review. Sie richtet sich an Autor:innen, Reviewer:innen und [inhaltsverantwortliche Rollen](glossar.md).

## Auslöser

* Eine neue Handbuch-Seite ist nötig (Bedarf erkannt, neue Aufgabe, neues Tool).
* Eine bestehende Seite muss aktualisiert werden (Prozessänderung, Tool-Wechsel, Fehler).
* Eine Seite ist zur regelmässigen Prüfung fällig.

## Beteiligte Rollen

| Rolle | Aufgabe |
|---|---|
| **Autor:in** | Schreibt den Entwurf, pflegt die Seite. |
| **Reviewer:in** | Prüft fachlich und gemäss Schreibregeln. |
| **Inhaltsverantwortliche Rolle** | Erteilt Freigabe zur Veröffentlichung; ist langfristig für die Korrektheit der Seite zuständig. Welche Rolle dies konkret ist, hängt vom Inhaltsbereich ab (z.B. Technik, Organisation, Mitgliederwesen). |

Wir ordnen Verantwortlichkeiten über Rollen zu, nicht über Personen (Prinzip P7 aus den [Leitprinzipien](leitprinzipien.md)). Welche Person aktuell welche Rolle innehat, pflegen wir zentral an einer Stelle.

## Ablauf

### Erstellung einer neuen Seite

Der Erstellungsprozess folgt einem schlanken, an [ISO/IEC/IEEE 26515:2018](https://www.iso.org/standard/70880.html) angelehnten Vorgehen für agile Dokumentationsentwicklung.

1. **Bedarf klären.** Welche Frage soll die Seite beantworten? Für wen?
2. **Seitentyp festlegen** nach [Inhaltstypen und Vorlagen](inhaltstypen-und-vorlagen.md). Bei Mischform: aufteilen.
3. **Vorlage wählen** aus [Inhaltstypen und Vorlagen](inhaltstypen-und-vorlagen.md).
4. **Entwurf schreiben** nach den [Schreibregeln und Markdown-Konventionen](schreibregeln-und-markdown.md).
5. **Selbst-Check** mit der Review-Checkliste (siehe unten).
6. **Peer-Review** durch mindestens eine weitere Person, die das Thema fachlich kennt.
7. **Freigabe** durch die inhaltsverantwortliche Rolle.
8. **Veröffentlichung** in WordPress.
9. **Metadaten setzen** (verantwortliche Rolle, Datum letzte Aktualisierung, Datum letzte Prüfung).

### Pflege bestehender Seiten

<details>
<summary>Leitsatz zum Pflegeprozess</summary>

Dokumentation ohne Pflege wird falsch. Falsche Dokumentation ist schlechter als keine.

</details>

#### Verteilte Verantwortung

Es gibt **keine einzelne Rolle, die für das gesamte Handbuch verantwortlich ist**. Wir verteilen die Verantwortung nach Inhaltsbereichen: Jede Seite hat eine inhaltsverantwortliche Rolle, die in den Metadaten der Seite genannt ist. Diese Rolle pflegt die Seite.

#### Regelmässige Prüfung

Jede Seite wird **regelmässig** durch die zuständige Rolle auf Aktualität geprüft. Was „regelmässig" konkret bedeutet, ergibt sich aus dem Inhaltsbereich:

* Seiten zu **schnell veränderlichen Themen** (z.B. genutzte Tools, externe Dienste) prüfen wir häufiger.
* Seiten zu **stabilen Themen** (z.B. Grundsätze, Organisationsstruktur) prüfen wir seltener.

Das Datum der letzten Prüfung steht in den Metadaten am Seitenende. So kann jede:r erkennen, wie aktuell eine Information ist, auch wenn keine inhaltliche Änderung nötig war.

#### Anlassbezogene Aktualisierung

Eine Seite wird **sofort** aktualisiert, wenn:

* sich ein Prozess ändert,
* ein Tool gewechselt oder eingestellt wird,
* ein Fehler in der Dokumentation gefunden wird,
* mehrere Personen die gleiche Frage stellen, weil das Handbuch sie nicht beantwortet.

Wer einen Fehler oder eine veraltete Information bemerkt, meldet das der inhaltsverantwortlichen Rolle der betroffenen Seite oder behebt es selbst (mit anschliessendem Review).

#### Versionierung

Da wir das Handbuch in WordPress veröffentlichen, nutzen wir die WordPress-Revisionen als technische Versionierung. Inhaltlich wichtige Änderungen halten wir in einem **Änderungsprotokoll** auf der jeweiligen Seite (am Ende, im Aufklappbereich) fest, jedoch nur, wenn die Änderung für Lesende relevant ist (z.B. geänderter Ablauf), nicht für reine Tippfehler.

## Review-Checkliste

Diese Checkliste ist die Grundlage von Selbst-Check und Peer-Review. Sie ist bewusst kurz gehalten.

### Inhalt

* [ ] Der **Seitentyp** ist klar erkennbar (Anleitung / Prozess / Übersicht / Rolle / Hintergrund).
* [ ] Die Seite hat **einen Hauptzweck** (kein Mischmasch).
* [ ] Die Information ist **fachlich korrekt** und **aktuell**.
* [ ] Externe Tool-Inhalte sind **verlinkt, nicht kopiert**.

### Struktur

* [ ] **Titel** ist aussagekräftig und aufgabenorientiert.
* [ ] **Kurzbeschreibung** beantwortet „Was?" und „Für wen?".
* [ ] **Aufklappbereiche** enthalten nur ergänzende, keine kritischen Inhalte.
* [ ] **Aufklappbereiche** sind nicht verschachtelt.
* [ ] **Erste Überschrift im Inhalt ist `##`**, keine `#` im Inhalt.
* [ ] **Metadaten** (verantwortliche Rolle, Datum letzte Aktualisierung, Datum letzte Prüfung) sind gesetzt.
* [ ] **Verantwortlichkeit** ist über eine Rolle zugewiesen, nicht über eine Person.

### Sprache

* [ ] Aktiv-Konstruktion und Imperativ verwendet (wo zutreffend).
* [ ] Sätze sind kurz und klar.
* [ ] Begriffe werden konsistent verwendet (Glossar geprüft).
* [ ] Keine Füllwörter, keine doppelten Verneinungen.

### Auffindbarkeit

* [ ] Die Seite ist mit verwandten Seiten **verlinkt**.
* [ ] Begriffe, die im Glossar stehen, sind beim ersten Vorkommen verlinkt.

## Ergebnis

Eine Handbuch-Seite, die freigegeben, veröffentlicht und gepflegt ist. Korrektheit, Aktualität und Verständlichkeit sind durch Selbst-Check, Peer-Review und Freigabe abgesichert.

## Verwandte Seiten

* [Regelwerk-Übersicht](WordPress-Training-Team-DACH/GitHub-Repo/learn-wp-dach-team/handbuch/Handbuch/README.md)
* [Leitprinzipien](leitprinzipien.md) – Prinzipien P6 und P7 prägen den Pflegeprozess
* [Inhaltstypen und Vorlagen](inhaltstypen-und-vorlagen.md) – Schritt 2 und 3 des Erstellungsprozesses
* [Schreibregeln und Markdown-Konventionen](schreibregeln-und-markdown.md) – Schritt 4 des Erstellungsprozesses
* [Glossar](glossar.md)

## Metadaten

*Verantwortliche Rolle: GitHub-Spezialist · Letzte Aktualisierung: 2026-05-03 · Letzte Prüfung: 2026-05-03*
