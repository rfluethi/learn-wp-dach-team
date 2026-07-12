# Schreibregeln und Markdown-Konventionen

## Kurzbeschreibung

Diese Seite legt die verbindlichen Schreibregeln, Terminologie-Konventionen und Markdown-Konventionen für alle Handbuch-Seiten fest. Sie richtet sich an Autor:innen und Reviewer:innen.

## Wer nutzt es

Alle Personen, die Inhalte verfassen, formatieren oder reviewen. Beim Schreiben jeder Seite anwendbar.

## Sprache und Stil

Die folgenden Regeln sind eine vereinfachte Auswahl aus der [tekom-Leitlinie „Regelbasiertes Schreiben, Deutsch für die Technische Kommunikation"](https://www.tekom.de/fileadmin/tekom.de/Die_tekom/Publikationen/Leseproben/2013_RBS_Deutsch_fuer_die_TK_Leseprobe.pdf) und dem internationalen Standard [IEC/IEEE 82079-1](https://de.wikipedia.org/wiki/IEC/IEEE_82079).

### Grundregeln

**S1, Aktiv statt passiv.**
Richtig: „Klicke auf *Speichern*."
Falsch: „Auf *Speichern* muss geklickt werden."

**S2, Kurze Sätze.**
Faustregel: ein Gedanke pro Satz. Sätze über 25 Wörter prüfen und meist teilen.

**S3, Imperativ in Anleitungen.**
Anleitungsschritte sind Befehle: „Öffne…", „Wähle…", „Speichere…". Standardsatzmuster für Schritte: Verb zuerst, ein Schritt, eine Handlung, sichtbares Ergebnis benennen.

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

**S9, Rechtschreibung.**
Amtliche deutsche Rechtschreibung **mit ß** („regelmäßig", „heißt"). Die Schweizer Schreibweise (ss statt ß) wird im Handbuch nicht verwendet. Prüfe Entwürfe aktiv darauf; „grosse", „heisst" sind häufige Fehler aus Schweizer Tastaturen.

## Terminologie und Konsistenz

**Seiten-Glossar pflegen:** Begriffe, die eine Seite spezifisch verwendet (Tool-Begriffe, Rollenbezeichnungen, interne Abkürzungen), definiert die Seite selbst in ihrem Seiten-Glossar am Ende, vor dem Transport-Block. Es gibt bewusst **kein zentrales Begriffsregister**: Taucht derselbe Begriff auf mehreren Seiten auf, wird dieselbe Definition wortgleich wiederverwendet (die einzige erlaubte Ausnahme vom Prinzip der einen Quelle, P5).

**Schreibweisen festlegen:** Tool- und Eigennamen schreiben wir in der vom Hersteller verwendeten Schreibweise (z.B. „WordPress", nicht „Wordpress" oder „wordpress").

**Konsistenz vor Eleganz:** Wenn zwei Formulierungen gleich gut wären, gewinnt die, die wir bereits verwenden.

**Verweise immer als Link:** Nie „siehe Anleitung, Kapitel 3", Kapitelnummern oder blosse Dateinamen; immer den klickbaren Link auf die Zielseite setzen.

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

**Praktisch heißt das:**
Eine „Tool-Übersicht"-Seite enthält:

1. Wofür wir das Tool nutzen (1 bis 3 Sätze).
2. Wer Zugang erhält und wie.
3. Unsere Konventionen (z.B. Namensschemata, Ordnerstruktur).
4. Verlinkung der offiziellen Dokumentation.
5. Verlinkung unserer eigenen Anleitungen, die dieses Tool betreffen.

**Vorteil:** Wenn der Hersteller seine Doku aktualisiert, profitieren wir automatisch. Wir pflegen nur die Stellen, die wir wirklich selbst kontrollieren.

## Markdown-Konventionen

### Dateiname = WordPress-Slug

Der Dateiname eines Entwurfs ist der spätere WordPress-Slug der Seite: Kleinbuchstaben, Bindestriche, keine Umlaute, keine Leerzeichen (z.B. `handbuch-seite-anlegen.md`). So ist jeder interne Link mechanisch in einen WordPress-Link übersetzbar. **Ausnahme:** Die Startseite eines Bereichs ist immer die `README.md`; ihr Slug ist der Bereichsname in Slug-Form und steht im Transport-Block in der Zusatzzeile `Slug:`.

### Überschriften

* Der Seitentitel steht im Entwurf als `#` (H1) zuoberst; der Markdown-Import übernimmt ihn als WordPress-Seitentitel.
* Im Inhalt darunter beginnt die Gliederung bei `##`; keine weitere H1 im Inhalt (doppelte H1 bricht Seitenstruktur, SEO und Barrierefreiheit).
* `##` für Hauptabschnitte, `###` für Unterabschnitte, maximal vier Ebenen.

### Aufklappbereiche

Da wir das Handbuch in WordPress veröffentlichen, verwenden wir HTML innerhalb des Markdowns:

```html
<details>
<summary>Kategorie: worum es geht</summary>

Inhalt des Aufklappbereichs in normalem Markdown.

</details>
```

* **Titel nach dem Muster „Kategorie: worum es geht"** (z.B. „Hintergrund: Wozu Labels dienen", „Hinweis: Wartung der View-Links"). Die Kategorie ordnet ein, der Teil nach dem Doppelpunkt sagt konkret, worum es geht. Generische Sammeltitel wie „Für neue Mitglieder" sind ausgeschlossen. Ausnahme: FAQ-Seiten, dort ist der Titel die Frage.
* **Formatierung (Pflicht):** Nach `</summary>` und vor `</details>` je eine Leerzeile, sonst rendert GitHub den Markdown-Inhalt nicht. Inhalt in normalem Markdown, kein zusätzliches HTML im Block.
* Beim Übertrag nach WordPress wird jedes `<details>` ein **Details-Block**.

Wann und wie Aufklappbereiche eingesetzt werden, steht in [Inhaltstypen und Vorlagen](inhaltstypen-und-vorlagen.md).

### Diagramme

* **Mermaid statt ASCII (Pflicht).** ASCII-Diagramme rendern auf den Handbuch-Seiten schlecht und sind verboten. Diagramme entstehen als Mermaid-Codeblock (```` ```mermaid ````); der Markdown-Import macht daraus einen gerenderten Mermaid-Block.
* **Aktiv einsetzen**, wo ein Diagramm die Beschreibung verdeutlicht und kürzt (Abläufe mit Übergaben, Zustandswechsel, Hierarchien). Das Diagramm ersetzt Text, es verdoppelt ihn nicht (P5).
* **Vektorgrafiken (SVG)** für Inhalte, die Mermaid nicht abbilden kann, im `assets`-Ordner des Bereichs ablegen und mit Alt-Text einbinden.

### Listen

* **Aufzählungen** mit `*` (Sternchen, einheitlich).
* **Nummerierte Listen** nur bei Schrittfolgen, in denen die Reihenfolge zwingend ist.
* Pro Listenpunkt ein Gedanke; sonst Fließtext oder Unterliste.

### Links

* **Interne Links** auf andere Handbuch-Seiten: relativer `.md`-Link auf die Zieldatei (funktioniert auf GitHub; beim Erfassen werden sie anhand der Slug-Konvention konvertiert).
* **Externe Links** (Hersteller-Dokus, Quellen) immer mit vollem URL; Linktext beschreibt das Ziel: richtig: „[Diátaxis-Framework](https://diataxis.fr/)"; falsch: „[hier klicken](https://...)".
* **Externe Links müssen verifiziert sein:** vor der Übergabe aufrufen und prüfen; bevorzugt offizielle, stabile Quellen. Wo immer möglich eine vertiefende externe Quelle anbieten.
* **Informieren, nicht verkaufen:** Keine Shop- oder Katalogseiten verlinken (z.B. Normen-Verkaufsportale). Stattdessen informierende Quellen: freie Spezifikationen, Wikipedia-Artikel, frei lesbare Norm-Auszüge.
* **Verweise immer als Link**, nie als Kapitelnummer oder blosser Dateiname ohne Link.

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

### Transport-Block

Jeder Markdown-Entwurf endet mit dem **Transport-Block**: Er trägt Seitentyp, verantwortliche Rolle, Themengebiet, Zielgruppe, Eltern-Seite, Reihenfolge, Textauszug und Aktualitäts-Daten. Beim Erfassen wird er in Felder übertragen und aus dem Inhalt gelöscht. Das exakte Muster steht in [markdown-konventionen.md](handbuch-autor/references/markdown-konventionen.md) des Skills.

## Verwandte Seiten

* [Regelwerk-Übersicht](README.md)
* [Leitprinzipien](leitprinzipien.md) – warum wir diese Regeln haben (P2, P5, P8)
* [Inhaltstypen und Vorlagen](inhaltstypen-und-vorlagen.md) – wann und wie Aufklappbereiche eingesetzt werden

## Seiten-Glossar

| Begriff | Definition |
|---|---|
| Seiten-Glossar | Tabelle am Ende einer Seite (vor dem Transport-Block), die die Fachbegriffe dieser Seite verbindlich definiert. |
| Transport-Block | Block am Ende jedes Markdown-Entwurfs, der die Metadaten zur Erfassung transportiert; wird beim Import in WordPress-Felder übertragen und aus dem Inhalt gelöscht. |

## Transport-Metadaten (beim Erfassen in Felder übertragen, dann diesen Block löschen)

* Seitentyp: Hintergrund/Konzept
* Verantwortliche Rolle: GitHub-Spezialist
* Themengebiet: Organisation
* Zielgruppe: Inhalts-Ersteller:innen
* Eltern-Seite: Handbuch-Erstellung
* Reihenfolge: 30
* Textauszug: Diese Seite legt die verbindlichen Schreibregeln, Terminologie-Konventionen und Markdown-Konventionen für alle Handbuch-Seiten fest.
* Letzte Aktualisierung: 2026-07-12
* Letzte Prüfung: 2026-05-03
* Prüfintervall: 365
