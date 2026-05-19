## Kurzbeschreibung

Diese Seite legt die verbindlichen Schreibregeln, Terminologie-Konventionen und Markdown-Konventionen für alle Handbuch-Seiten fest. Sie richtet sich an Autor:innen und Reviewer:innen.

## Wer nutzt es

Alle Personen, die Inhalte verfassen, formatieren oder reviewen. Beim Schreiben jeder Seite anwendbar.

## Sprache und Stil

Die folgenden Regeln sind eine vereinfachte Auswahl aus der [tekom-Leitlinie „Regelbasiertes Schreiben, Deutsch für die Technische Kommunikation"](https://www.tekom.de/fileadmin/tekom.de/Die_tekom/Publikationen/Leseproben/2013_RBS_Deutsch_fuer_die_TK_Leseprobe.pdf) und dem internationalen Standard [IEC/IEEE 82079-1](https://www.iso.org/standard/71620.html).

### Grundregeln

**S1, Aktiv statt passiv.**
Richtig: „Klicke auf *Speichern*."
Falsch: „Auf *Speichern* muss geklickt werden."

**S2, Kurze Sätze.**
Faustregel: ein Gedanke pro Satz. Sätze über 25 Wörter prüfen und meist teilen.

**S3, Imperativ in Anleitungen.**
Anleitungsschritte sind Befehle: „Öffne…", „Wähle…", „Speichere…".

**S4, Konkrete Wörter statt abstrakter.**
Richtig: „Das Formular"
Falsch: „Die entsprechende Eingabemaske"

**S5, Eine Bedeutung, ein Begriff.**
Verwende für dieselbe Sache immer dasselbe Wort. Nicht abwechselnd „Mitglied", „Person", „Teilnehmer:in", wenn dasselbe gemeint ist (siehe Abschnitt *Terminologie* weiter unten).

**S6, Anrede konsistent.**
In Anleitungen sprechen wir die lesende Person mit „du" (kleingeschrieben) an. Konventionen formulieren wir mit „wir". Regeln und Kriterien stehen unpersönlich. Diese Trennung halten wir konsistent über alle Seiten ein.

**S7, Keine Füllwörter.**
Streiche „eigentlich", „grundsätzlich", „im Prinzip", „natürlich".

**S8, Gendergerecht und lesbar.**
Wir verwenden den Doppelpunkt („Mitarbeiter:innen") oder geschlechtsneutrale Formulierungen („das Team", „die Mitglieder"). Konsistent über alle Seiten.

## Terminologie und Konsistenz

**Glossar pflegen:** Begriffe, die wir spezifisch verwenden (Tool-Namen, Rollenbezeichnungen, interne Abkürzungen), definieren wir zentral im [Glossar](glossar.md). Bei der ersten Verwendung auf einer Seite verlinken wir aufs Glossar.

**Schreibweisen festlegen:** Tool- und Eigennamen schreiben wir in der vom Hersteller verwendeten Schreibweise (z.B. „WordPress", nicht „Wordpress" oder „wordpress").

**Konsistenz vor Eleganz:** Wenn zwei Formulierungen gleich gut wären, gewinnt die, die wir bereits verwenden.

<details>
<summary>Weiterführend: Warum Terminologiekontrolle?</summary>

Inkonsistente Begriffe sind die häufigste Ursache für Missverständnisse in technischer Dokumentation. Die [tekom-Leitlinie](https://www.tekom.de/fileadmin/tekom.de/Die_tekom/Publikationen/Leseproben/2013_RBS_Deutsch_fuer_die_TK_Leseprobe.pdf) empfiehlt explizit eine Terminologieliste als Grundlage konsistenter Texte.

</details>

## Umgang mit externen Tool-Dokumentationen

**Wir duplizieren keine Hersteller-Dokumentation** (Prinzip P2 aus den [Leitprinzipien](leitprinzipien.md)). Stattdessen:

| Wir dokumentieren | Wir verlinken |
|---|---|
| Wie **wir als Gruppe** das Tool einsetzen | Wie das Tool grundsätzlich funktioniert |
| Unsere **spezifischen Konfigurationen** und Konventionen | Hersteller-Tutorials und Referenzen |
| Unsere **Prozesse**, in denen das Tool vorkommt | Allgemeine Funktionsbeschreibungen |
| **Wann** wir welches Tool wofür nutzen | Versionshinweise des Herstellers |

**Praktisch heisst das:**
Eine „Tool-Übersicht"-Seite enthält:

1. Wofür wir das Tool nutzen (1 bis 3 Sätze).
2. Wer Zugang erhält und wie.
3. Unsere Konventionen (z.B. Namensschemata, Ordnerstruktur).
4. Verlinkung der offiziellen Dokumentation.
5. Verlinkung unserer eigenen Anleitungen, die dieses Tool betreffen.

**Vorteil:** Wenn der Hersteller seine Doku aktualisiert, profitieren wir automatisch. Wir pflegen nur die Stellen, die wir wirklich selbst kontrollieren.

## Markdown-Konventionen

### Überschriften

* Eine `#`-Hauptüberschrift entsteht in WordPress automatisch aus dem Seitentitel.
* Im Markdown-Inhalt selbst beginnen wir deshalb immer mit `##` (zweite Ebene). Eine `#`-Überschrift im Inhalt würde zu einer doppelten H1 führen, das ist sowohl für SEO als auch für die Barrierefreiheit problematisch.
* `##` für Hauptabschnitte, `###` für Unterabschnitte.
* Maximal vier Ebenen (`####`); tiefer wird unübersichtlich.

### Aufklappbereich „Weitere Informationen"

Da wir das Handbuch in WordPress veröffentlichen, verwenden wir HTML innerhalb des Markdowns:

```html
<details>
<summary>Aussagekräftiger Titel des Aufklappbereichs</summary>

Inhalt des Aufklappbereichs in normalem Markdown.

</details>
```

Wann und wie Aufklappbereiche eingesetzt werden, steht in [Inhaltstypen und Vorlagen](inhaltstypen-und-vorlagen.md).

<details>
<summary>Hinweis zur WordPress-Umsetzung</summary>

Die genaue Umsetzung in WordPress (z.B. via Gutenberg-Block oder Plugin) klärt und dokumentiert die für die Handbuch-Infrastruktur verantwortliche Rolle.

</details>

### Listen

* **Aufzählungen** mit `*` (Sternchen, einheitlich).
* **Nummerierte Listen** nur bei Schrittfolgen, in denen die Reihenfolge zwingend ist.
* Pro Listenpunkt ein Gedanke; sonst Fliesstext oder Unterliste.

### Links

* **Interne Links** auf andere Handbuch-Seiten: relativer Pfad.
* **Externe Links** (Hersteller-Dokus, Quellen) immer mit vollem URL.
* Linktext beschreibt das Ziel: richtig: „[Diátaxis-Framework](https://diataxis.fr/)"; falsch: „[hier klicken](https://...)".

### Anker für Sprungziele

Wir nutzen für stabile Sprungziele manuelle HTML-Anker (`<a name="anker-name"></a>`) direkt nach der jeweiligen Überschrift. Begründung: Automatische Markdown-Anker können sich bei Umformulierung der Überschrift ändern und Links brechen.

### Code und Befehle

* Inline-Code mit Backticks: `` `Befehl` ``.
* Codeblöcke mit Sprachangabe für Syntax-Highlighting.

### Hervorhebungen

* **Fett** (`**...**`) für wichtige Begriffe und UI-Elemente.
* *Kursiv* (`*...*`) für Eigennamen, Zitate, Bildschirmbeschriftungen.
* Sparsam einsetzen: Wenn alles hervorgehoben ist, ist nichts hervorgehoben.

### Tabellen

Tabellen verwenden, wenn Inhalte vergleichend oder mehrdimensional sind. Bei einfachen Aufzählungen lieber Listen verwenden.

## Verwandte Seiten

* [Regelwerk-Übersicht](WordPress-Training-Team-DACH/GitHub-Repo/learn-wp-dach-team/handbuch/Handbuch/README.md)
* [Leitprinzipien](leitprinzipien.md) – warum wir diese Regeln haben (P2, P5, P8)
* [Inhaltstypen und Vorlagen](inhaltstypen-und-vorlagen.md) – wann und wie Aufklappbereiche eingesetzt werden
* [Glossar](glossar.md)

## Metadaten

*Verantwortliche Rolle: GitHub-Spezialist · Letzte Aktualisierung: 2026-05-03 · Letzte Prüfung: 2026-05-03*
