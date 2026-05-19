# Skill-Entwurf: handbuch-autor (v2)

> **Status:** Entwurf zum Testen, Version 2. Alle Skill-Bestandteile (SKILL.md plus Referenzdateien) sind in dieser einen Datei zusammengefasst und durch Trenner kenntlich gemacht. Vor dem Installieren als Skill müssen die Abschnitte in die in [Spätere Installation](#sp-tere-installation) beschriebene Ordnerstruktur aufgeteilt werden.

> **Änderungen gegenüber v1:** Eigener Workflow „Bestehenden Inhalt aufteilen" mit neuer Referenzdatei `references/aufteilen.md`. Der Workflow „Überarbeitung" verweist nun auf den Aufteilungs-Workflow, wenn eine Mischform erkannt wird.

> **Basis:** Die Anleitung zur Erstellung des Team-Handbuchs (Version 1.0).

## Hinweise zum Testen dieses Skill-Entwurfs

Ein Skill hat in seiner produktiven Form folgende Struktur:

```
handbuch-autor/
├── SKILL.md                       (Hauptdatei, wird immer geladen wenn Skill triggert)
└── references/
    ├── inhaltstypen.md            (welcher Seitentyp passt zur Anfrage?)
    ├── aufteilen.md               (Mischform erkennen und aufteilen)
    ├── vorlage-anleitung.md
    ├── vorlage-prozess.md
    ├── vorlage-tool.md
    ├── vorlage-rolle.md
    ├── vorlage-konzept.md
    ├── schreibregeln.md           (Sprache, Stil, Terminologie)
    ├── markdown-konventionen.md   (WordPress-spezifisches Markdown)
    └── review-checkliste.md
```

Diese Datei enthält alle diese Abschnitte in einer einzigen Markdown-Datei zum Lesen und Testen. Jeder Abschnitt ist mit `=== DATEI: <pfad> ===` markiert.

# === DATEI: SKILL.md ===

```yaml
---
name: handbuch-autor
description: Erstellt, prüft, überarbeitet und teilt Inhalte für unser Team-Handbuch auf. Setze diesen Skill IMMER ein, wenn der Mensch eine Handbuch-Seite schreiben, überarbeiten, prüfen, strukturieren oder bestehenden Inhalt aufteilen will, oder wenn von "Anleitung", "How-to", "Prozessbeschreibung", "Tool-Übersicht", "Rollenbeschreibung" oder "Hintergrundseite" für das interne Handbuch die Rede ist. Nutze ihn auch, wenn der Mensch nur sagt "ich muss noch was fürs Handbuch schreiben", "kannst du das fürs Wiki dokumentieren" oder "diese Seite ist ein Mischmasch, kannst du sie aufräumen", ohne den Seitentyp explizit zu nennen. Der Skill stellt sicher, dass jede Seite den Grundsätzen unseres Handbuch-Konzepts folgt: ein Hauptzweck pro Seite (Diátaxis), Progressive Disclosure für die Doppel-Zielgruppe Onboarding/Nachschlagen, Verlinkung statt Duplizierung externer Dokumentationen, Verantwortlichkeit über Rollen, und konsistente Markdown-Struktur für die WordPress-Veröffentlichung. Bei bestehenden, gemischten Inhalten erkennt der Skill Mischformen, schlägt eine Aufteilung in saubere Einzelseiten vor und führt sie nach Bestätigung aus.
---
```

# Skill: handbuch-autor

Dieser Skill unterstützt beim Erstellen, Prüfen, Überarbeiten und **Aufteilen** von Seiten für unser Team-Handbuch. Er sorgt dafür, dass jede Seite den vereinbarten Grundsätzen folgt und in Markdown für die WordPress-Veröffentlichung sauber aufgebaut ist.

## Wann triggern

Setze diesen Skill ein, sobald jemand:

* eine **neue Seite** für das Handbuch schreiben will,
* eine **bestehende Seite überarbeiten** möchte,
* eine Seite **reviewen** oder gegen die Qualitätskriterien prüfen will,
* einen **bestehenden, gemischten Inhalt aufteilen** will (z.B. eine alte Wiki-Seite, die mehrere Themen vermischt),
* unsicher ist, ob ein Inhalt überhaupt ins Handbuch gehört oder wie er strukturiert werden soll,
* allgemein über „Doku", „Anleitung", „Prozess dokumentieren", „Wiki-Eintrag", „aufräumen" oder „fürs Handbuch" spricht, auch wenn der Begriff „Skill" oder „Handbuch-Autor" nicht fällt.

## Grundsätze, die dieser Skill konsequent umsetzt

Diese Grundsätze stammen aus der Anleitung zur Erstellung des Team-Handbuchs. Sie sind das Fundament aller folgenden Schritte. Halte dich an sie auch dann, wenn der Mensch sie nicht explizit nennt.

* **P1, ein Hauptzweck pro Seite** ([Diátaxis-Framework](https://diataxis.fr/)). Eine Seite ist Anleitung **oder** Erklärung **oder** Nachschlagewerk, nicht alles gleichzeitig.
* **P2, nicht duplizieren, verlinken.** Hersteller-Dokumentationen werden verlinkt, nie kopiert. Wir dokumentieren nur, was unsere Gruppe spezifisch betrifft.
* **P3, Progressive Disclosure.** Pflichtinformationen sichtbar, Hintergrund/Begründungen in `<details>`-Aufklappbereichen.
* **P4, Aktion vor Theorie.** Bei Anleitungen kommt zuerst, was zu tun ist. Das Warum folgt im Aufklappbereich.
* **P5, Single Source of Truth.** Jede Information existiert genau einmal; andere Stellen verlinken.
* **P6, Aktualität sichtbar machen.** Jede Seite hat am Ende Metadaten: verantwortliche Rolle, letzte Aktualisierung, letzte Prüfung.
* **P7, Rollen statt Personen.** Verantwortlichkeiten werden über Rollen zugewiesen, nie über konkrete Namen.
* **P8, Nutzerperspektive vor Tool-Logik.** Anleitungen sind nach Aufgaben strukturiert, nicht nach Tool-Menüs.

## Arbeitsmodus: zwei Wege je nach Bedarf

Dieser Skill kennt zwei Modi. Wähle den passenden auf Basis der Anfrage; bei Unsicherheit kläre kurz mit dem Menschen.

### Modus A, beratend („KI fragt, schlägt vor, Mensch entscheidet")

Nutze diesen Modus, wenn:

* das Thema **fachlich komplex** ist und der Mensch die Antworten kennt, du aber nicht,
* die Seite **organisatorische Festlegungen** enthält (Rollen, Verantwortlichkeiten, Befugnisse),
* der Mensch **Unsicherheit** signalisiert oder ausdrücklich gemeinsam entwickeln will,
* eine **Aufteilung** bestehender Inhalte ansteht (immer beratend, weil Strukturentscheidung).

Vorgehen: Stelle gezielte Fragen, formuliere Vorschläge zur Struktur, lass den Menschen entscheiden, schreibe dann den Entwurf.

### Modus B, generierend („KI erstellt direkt einen Entwurf")

Nutze diesen Modus, wenn:

* der Mensch eine **klare Aufgabe** beschreibt („Schreib eine Anleitung, wie man X macht"),
* die nötigen Informationen **bereits im Gespräch** stehen (etwa als Notizen oder grober Entwurf),
* der Mensch ausdrücklich um einen **direkten Entwurf** bittet.

Vorgehen: Erstelle direkt einen vollständigen Markdown-Entwurf nach der passenden Vorlage. Markiere alle Stellen, an denen du geraten oder Annahmen getroffen hast, mit `[ANNAHME: …]`, damit der Mensch gezielt prüfen kann.

**Nicht raten bei:** verantwortlichen Rollen, internen Tool-Konventionen, organisatorischen Abläufen. Diese müssen vom Menschen kommen oder als Platzhalter `[Rolle]`, `[wird ergänzt]` markiert werden.

## Die vier Workflows im Überblick

| Workflow | Wann einsetzen |
|---|---|
| [W1, neue Seite](#w1-neue-seite) | Es gibt noch keinen Inhalt; eine Seite soll von Grund auf entstehen. |
| [W2, bestehende Seite überarbeiten](#w2-bestehende-seite-überarbeiten) | Inhalt existiert, Seitentyp ist eindeutig, nur die Form soll verbessert werden. |
| [W3, bestehenden Inhalt aufteilen](#w3-bestehenden-inhalt-aufteilen) | Inhalt existiert, vermischt aber mehrere Seitentypen oder Themen. |
| [W4, Review](#w4-review) | Nur prüfen, nicht ändern. Befunde melden. |

**Wichtig:** Bei einer Anfrage zur Überarbeitung (W2) prüfst du immer **zuerst**, ob es sich tatsächlich um W2 handelt oder ob in Wahrheit W3 nötig ist. Diese Entscheidung trifft `references/aufteilen.md`.

## W1, neue Seite

Folge diesen Schritten in dieser Reihenfolge. Überspringe keinen.

### Schritt 1, Seitentyp bestimmen

Lade `references/inhaltstypen.md` und prüfe die Anfrage gegen die Entscheidungsfragen dort. Wenn du **mehrere** Seitentypen passend findest, ist die Anfrage vermutlich eine Mischform und sollte aufgeteilt werden. Frage in diesem Fall nach.

### Schritt 2, passende Vorlage laden

Sobald der Seitentyp feststeht, lade **nur die passende** Vorlagedatei:

| Seitentyp | Referenzdatei |
|---|---|
| Anleitung (How-to) | `references/vorlage-anleitung.md` |
| Prozessbeschreibung | `references/vorlage-prozess.md` |
| Tool-Übersicht | `references/vorlage-tool.md` |
| Rollen- / Organisationsbeschreibung | `references/vorlage-rolle.md` |
| Hintergrund / Konzept | `references/vorlage-konzept.md` |

### Schritt 3, Inhalte sammeln (Modus A) oder direkt entwerfen (Modus B)

Folge dem in der Vorlagedatei beschriebenen Frageleitfaden bzw. erstelle den Entwurf direkt.

### Schritt 4, Schreibregeln anwenden

Lade `references/schreibregeln.md` und wende sie auf den Entwurf an.

### Schritt 5, Markdown-Konventionen prüfen

Lade `references/markdown-konventionen.md` und prüfe.

### Schritt 6, Selbst-Check mit Review-Checkliste

Lade `references/review-checkliste.md` und prüfe den Entwurf systematisch durch.

### Schritt 7, Übergabe

Liefere dem Menschen den fertigen Entwurf. Nenne dabei:

* den gewählten **Seitentyp**,
* alle Stellen, die als **`[ANNAHME: …]`** markiert sind,
* alle Stellen, die als **`[Rolle]`**, **`[Datum]`** oder **`[wird ergänzt]`** Platzhalter enthalten,
* eine **kurze Begründung**, falls du an irgendeiner Stelle bewusst von einer Vorlage abgewichen bist.

## W2, bestehende Seite überarbeiten

### Schritt 1, vorhandenen Inhalt vollständig lesen

Lies den ganzen Inhalt, bevor du etwas tust. Springe nicht.

### Schritt 2, Mischform-Check (kritisch!)

**Bevor** du mit der eigentlichen Überarbeitung beginnst, lade `references/aufteilen.md` und prüfe den Inhalt gegen die dort beschriebenen Mischform-Symptome.

* **Keine Mischform erkannt:** Weiter mit Schritt 3 (W2).
* **Mischform erkannt:** Wechsle zu **Workflow W3, Aufteilen**. Erstelle keinen überarbeiteten Entwurf, bevor die Aufteilungsfrage geklärt ist.

### Schritt 3, Seitentyp bestätigen

Bestätige, dass der erkannte Seitentyp zur tatsächlichen Struktur passt. Lade `references/inhaltstypen.md` zur Kontrolle.

### Schritt 4, Vorlage laden und vergleichen

Lade die zum Seitentyp passende Vorlagedatei und vergleiche die Struktur. Liste Abweichungen auf.

### Schritt 5, Schreibregeln und Markdown-Konventionen anwenden

Lade `references/schreibregeln.md` und `references/markdown-konventionen.md`.

### Schritt 6, Übergabe mit Änderungsliste

Liefere die überarbeitete Fassung **plus eine kurze Liste der Änderungen** mit Begründung. So kann der Mensch nachvollziehen, was warum geändert wurde, und einzelne Änderungen ablehnen.

## W3, bestehenden Inhalt aufteilen

Dieser Workflow ist häufig: Bestehende Dokumentationen sind oft historisch gewachsen und vermischen Anleitung, Erklärung und Nachschlagewerk auf einer Seite. Saubere Trennung verbessert Auffindbarkeit und Pflegbarkeit.

**Wichtig:** Aufteilen ist immer Modus A (beratend). Die Strukturentscheidung trifft der Mensch.

### Schritt 1, vorhandenen Inhalt vollständig lesen

Lies den ganzen Inhalt sorgfältig.

### Schritt 2, Aufteilungs-Methode laden und anwenden

Lade `references/aufteilen.md` und folge der dort beschriebenen Methode:

1. Mischform-Symptome prüfen
2. Inhalt absatzweise klassifizieren
3. Cluster bilden (welche Absätze gehören zusammen?)
4. Vorgeschlagene Seitenstruktur ableiten

### Schritt 3, Aufteilungs-Vorschlag präsentieren

Präsentiere dem Menschen:

* welche **Mischform-Symptome** du erkannt hast,
* welchen **Aufteilungs-Vorschlag** du machst (z.B. „aus dieser einen Seite werden drei: eine Anleitung, eine Tool-Übersicht, eine Konzeptseite"),
* wie die neuen Seiten **untereinander verlinkt** werden sollen,
* welche **Inhalte ggf. wegfallen** (z.B. duplizierter Hersteller-Doku-Inhalt → Verlinkung),
* welche **Alternativen** es gibt (z.B. „statt aufteilen könnten wir auch nur Aufklappbereiche nutzen, das wäre weniger eingreifend").

### Schritt 4, Bestätigung abwarten

**Tue nichts, bevor der Mensch entschieden hat.** Mögliche Antworten:

* „Ja, teile auf wie vorgeschlagen": weiter mit Schritt 5.
* „Ja, aber anders": Vorschlag anpassen, neu vorlegen.
* „Nein, lass es zusammen": stattdessen W2 ausführen, ggf. mit Aufklappbereichen.

### Schritt 5, Aufteilung ausführen

Erstelle pro neuer Seite:

* einen **Markdown-Entwurf** nach der jeweils passenden Vorlage,
* eine **Verlinkungs-Übersicht** (welche Seite verweist auf welche),
* eine **Liste der Quellabsätze**, aus denen die neue Seite entstanden ist (zum Nachvollziehen).

### Schritt 6, Frage zur Weiterverarbeitung

Frage den Menschen, ob er möchte, dass du die einzelnen neuen Seiten direkt nach **W2** überarbeitest (Sprache, Schreibregeln, Markdown-Konventionen anwenden), oder ob er das selbst tun möchte. Beide Wege sind gültig:

* **„Direkt überarbeiten":** Fahre mit W2 für jede neue Seite fort.
* **„Erst nur aufteilen, ich überarbeite selbst":** Liefere die Rohaufteilung und stoppe.

## W4, Review

Wenn der Mensch nur ein Review (kein Rewrite) wünscht:

1. Bestimme den Seitentyp.
2. Prüfe, ob eine Mischform vorliegt (`references/aufteilen.md`). Falls ja: in den Befund aufnehmen.
3. Gehe `references/review-checkliste.md` Punkt für Punkt durch.
4. Liste **konkrete Funde** mit Verweis auf die Stelle (z.B. „Abschnitt ‚Schritte', Punkt 3: Passivkonstruktion, besser im Imperativ").
5. Schlage Verbesserungen vor, **schreibe aber nicht ungefragt um**.

## Was dieser Skill bewusst nicht tut

* Er **schreibt keine externen Hersteller-Dokumentationen ab**. Stattdessen verlinkt er sie. Dies entspricht Prinzip P2.
* Er **erfindet keine Rollennamen oder Verantwortlichkeiten**. Wenn diese unbekannt sind, werden Platzhalter `[Rolle]` gesetzt.
* Er **setzt keine Datumsangaben** ein, die er nicht kennt. „Letzte Prüfung" und „Letzte Aktualisierung" werden als Platzhalter `[JJJJ-MM-TT]` belassen, wenn das Datum nicht aus dem Gespräch hervorgeht.
* Er **teilt nicht ungefragt auf.** Aufteilung ist eine Strukturentscheidung, die der Mensch trifft.
* Er **verwendet keine Mischformen** zwischen Seitentypen. Lieber zwei kürzere Seiten als eine, die alles vermischt.

## Quellen, auf denen dieser Skill basiert

* Anleitung zur Erstellung des Team-Handbuchs (intern), Version 1.0
* [Diátaxis-Framework](https://diataxis.fr/) für die Inhaltstypen
* [Progressive Disclosure (Nielsen Norman Group)](https://www.nngroup.com/articles/progressive-disclosure/) für die Doppel-Zielgruppe-Lösung
* [tekom-Leitlinie „Regelbasiertes Schreiben"](https://www.tekom.de/fileadmin/tekom.de/Die_tekom/Publikationen/Leseproben/2013_RBS_Deutsch_fuer_die_TK_Leseprobe.pdf) für die deutschen Schreibregeln

# === DATEI: references/inhaltstypen.md ===

# Inhaltstypen bestimmen

Bevor eine Seite geschrieben wird, muss der Seitentyp feststehen. Das ist die wichtigste Strukturentscheidung, sie entscheidet über Aufbau, Tonalität und Vorlage.

## Die fünf Seitentypen

| Seitentyp | Diátaxis-Typ | Zweck | Beispieltitel |
|---|---|---|---|
| **Anleitung** | How-to-Guide | Eine konkrete Aufgabe Schritt für Schritt erledigen | „So legst du eine neue Mitgliederliste an" |
| **Prozessbeschreibung** | How-to-Guide | Wiederkehrenden Ablauf mit mehreren Beteiligten dokumentieren | „Aufnahme eines neuen Mitglieds" |
| **Tool-Übersicht** | Reference | Was wir nutzen, wofür, mit Verweis auf die Hersteller-Doku | „Übersicht: WordPress" |
| **Rollen- / Organisationsbeschreibung** | Reference / Explanation | Struktur der Gruppe, Verantwortlichkeiten | „Rolle: Mitgliederbetreuung" |
| **Hintergrund / Konzept** | Explanation | Warum-Fragen, Zusammenhänge, Designentscheidungen | „Warum wir Markdown verwenden" |

## Entscheidungsfragen

Beantworte diese Fragen in dieser Reihenfolge:

**Frage 1: Was tut die Lesende Person mit dieser Seite?**

* Eine Aufgabe **erledigen**? → Anleitung oder Prozessbeschreibung
* Etwas **nachschlagen**? → Tool-Übersicht oder Rollenbeschreibung
* Etwas **verstehen**? → Hintergrund / Konzept

**Frage 2: Wenn „erledigen", wie viele Personen sind beteiligt?**

* Eine Person, in einer Sitzung → **Anleitung**
* Mehrere Personen oder Rollen, eventuell über mehrere Tage → **Prozessbeschreibung**

**Frage 3: Wenn „nachschlagen", was ist das Subjekt?**

* Ein **Tool** → Tool-Übersicht
* Eine **Rolle** oder **Organisationseinheit** → Rollenbeschreibung

## Wenn der Seitentyp unklar ist

Stelle dem Menschen folgende Frage:

> „Was soll die Lesende Person mit dieser Seite tun: eine Aufgabe erledigen, etwas nachschlagen, oder etwas verstehen?"

Die Antwort führt direkt zur richtigen Kategorie.

## Wenn mehrere Seitentypen passen

Das ist ein Hinweis auf eine **Mischform**. Lade `references/aufteilen.md` und folge dem Workflow W3.

# === DATEI: references/aufteilen.md ===

# Mischform erkennen und bestehenden Inhalt aufteilen

Diese Referenz beschreibt, wie ein bestehender Inhalt analysiert und in saubere Einzelseiten aufgeteilt wird.

## Warum aufteilen wichtig ist

Mischformen verletzen Prinzip P1 („ein Hauptzweck pro Seite") und führen zu zwei Problemen:

* **Lesende finden nicht, was sie suchen.** Wer schnell nachschlagen will, muss durch Lernmaterial waten. Wer lernen will, stolpert über knappe Referenzen.
* **Pflege ist schwer.** Eine Seite, die fünf Themen mischt, hat fünf potenzielle Auslöser für Aktualisierung. Sauber getrennte Seiten haben jeweils einen.

## Phase 1, Mischform erkennen

Prüfe den Inhalt gegen folgende **Symptome**. Trifft auch nur **eines** klar zu, liegt eine Mischform vor.

### Symptom 1, Titel mit „und" oder mehreren Substantiven

Beispiele:

* „WordPress, Übersicht und Anleitung zum Login" → Tool-Übersicht **und** Anleitung
* „Mitgliederaufnahme, Prozess und Hintergründe" → Prozess **und** Konzept
* „Rolle Vorstand und Aufgaben im Jahreszyklus" → Rolle **und** Prozess

### Symptom 2, mehrere Diátaxis-Typen im selben Text

Prüfe absatzweise: Welcher der vier Diátaxis-Typen ist das?

* **Tutorial / Anleitung:** Schritt-für-Schritt, Imperativ, „Mache dies, dann das"
* **How-to / Prozess:** Aufgabenorientiert, mit Voraussetzungen und Ergebnis
* **Reference / Übersicht:** Nachschlagewerk, Listen, Tabellen, neutrale Beschreibung
* **Explanation / Hintergrund:** Begründungen, „Warum machen wir das so", Zusammenhänge

Wenn du im selben Text Absätze aus zwei oder mehr Kategorien findest, ist es eine Mischform.

### Symptom 3, Zielgruppenwechsel mitten im Text

Beispiel: Erst stehen sehr basale Erklärungen für Neue („Was ist überhaupt eine Mitgliederliste?"), dann kommen plötzlich knappe Power-User-Befehle ohne Kontext. Das deutet darauf hin, dass zwei Zielgruppen auf einer Seite bedient werden, was unsere [Progressive Disclosure-Lösung](https://www.nngroup.com/articles/progressive-disclosure/) (sichtbarer Pflichtweg + Aufklappbereich) eleganter löst als ein Mischtext.

### Symptom 4, „Außerdem"-Absätze

Begriffe wie „Außerdem", „Übrigens", „In diesem Zusammenhang", „Ergänzend" leiten oft Inhalte ein, die thematisch eigentlich nicht mehr zur Hauptseite gehören. Solche Absätze sind Kandidaten für Auslagerung.

### Symptom 5, langer „Hintergrund"-Block in einer Anleitung

Wenn eine Anleitung mehr als ein paar Sätze Hintergrundinformation enthält, gehört dieser Block entweder in einen `<details>`-Aufklappbereich oder, falls länger und eigenständig wertvoll, in eine eigene Konzeptseite mit Verlinkung.

### Symptom 6, abgeschriebene Hersteller-Dokumentation

Wenn ein Abschnitt im Wesentlichen nacherzählt, was beim Hersteller steht, verletzt das Prinzip P2 („nicht duplizieren, verlinken"). Dieser Abschnitt entfällt in der Aufteilung und wird durch einen Verweis auf die Hersteller-Doku ersetzt.

## Phase 2, Inhalt klassifizieren

Sobald eine Mischform erkannt ist, klassifiziere den Inhalt **absatzweise**.

### Vorgehen

1. Nummeriere die Absätze gedanklich durch.
2. Weise jedem Absatz einen der fünf Seitentypen zu (oder „entfällt", falls Hersteller-Doku-Duplikat).
3. Notiere unsichere Zuordnungen mit Begründung.

### Beispiel

> Originaltext: „WordPress ist unser zentrales CMS. Die Hersteller-Doku findet sich unter wordpress.org. Bei uns nutzt es die Redaktion. Um einen Beitrag anzulegen, klicke auf ‚Neu' und wähle ‚Beitrag'. Dann fülle Titel und Inhalt aus. Wir haben uns für WordPress entschieden, weil es OpenSource ist und eine grosse Community hat."

Klassifikation:

| Absatz | Inhalt | Klassifikation |
|---|---|---|
| 1 | „WordPress ist unser zentrales CMS." | Tool-Übersicht |
| 2 | „Hersteller-Doku unter wordpress.org" | Tool-Übersicht (Verlinkung) |
| 3 | „Bei uns nutzt es die Redaktion" | Tool-Übersicht (Wer nutzt es) |
| 4-5 | „Um einen Beitrag anzulegen, klicke auf …" | Anleitung |
| 6 | „Wir haben uns entschieden, weil OpenSource" | Hintergrund / Konzept |

## Phase 3, Cluster bilden und Seitenstruktur ableiten

Fasse Absätze derselben Klassifikation zu **Clustern** zusammen. Jedes Cluster wird tendenziell eine eigene Seite.

### Entscheidungshilfe: aufteilen oder nicht?

Aufteilung lohnt sich, wenn **mindestens eins** zutrifft:

* Ein Cluster hat genug Substanz für eine eigenständige Seite (mehr als 2-3 Absätze).
* Die Inhalte werden voraussichtlich **unabhängig voneinander** aktualisiert.
* Die Inhalte richten sich an **unterschiedliche Lesesituationen** (eine Person sucht „Wie geht das?", eine andere „Warum ist das so?").

Aufteilung lohnt sich **nicht**, wenn:

* Ein Cluster nur aus 1-2 Sätzen besteht: dann besser als Aufklappbereich integrieren.
* Die Inhalte nur **gemeinsam** Sinn ergeben (z.B. ein sehr kurzer Prozess mit untrennbarem Hintergrund).
* Die Hauptseite dadurch zu **dünn** würde (eine Seite mit nur einem Satz Inhalt ist auch keine Lösung).

### Beispiel-Aufteilung

Aus dem WordPress-Beispiel oben:

| Neue Seite | Seitentyp | Quellabsätze |
|---|---|---|
| „Übersicht: WordPress" | Tool-Übersicht | 1, 2, 3 |
| „So legst du einen WordPress-Beitrag an" | Anleitung | 4, 5 |
| „Warum WordPress" | Hintergrund / Konzept | 6 |

## Phase 4, Verlinkungsmuster

Nach dem Aufteilen müssen die neuen Seiten sinnvoll verlinkt werden. Standard-Muster:

### Tool-Übersicht als Knotenpunkt

Die Tool-Übersicht („Übersicht: WordPress") verlinkt auf:

* die offizielle Hersteller-Doku (extern)
* alle Anleitungen, die dieses Tool nutzen (intern)
* die Konzeptseite mit der Auswahl-Begründung (intern)

### Anleitung verweist nach oben

Eine Anleitung verlinkt im Bereich „Verwandte Seiten":

* die Tool-Übersicht des verwendeten Tools
* andere Anleitungen, die in derselben Aufgabenkette stehen

### Konzeptseite als Begründungsanker

Konzeptseiten („Warum WordPress") werden vor allem aus Aufklappbereichen anderer Seiten verlinkt, nicht im Hauptfluss. Sie sind die „Tiefe" hinter den praktischen Seiten.

## Phase 5, Vorschlag formulieren

Wenn du dem Menschen einen Aufteilungsvorschlag machst, strukturiere ihn so:

```markdown
## Mischform-Befund

Ich habe folgende Symptome erkannt:
- [Symptom mit Beispielzitat aus dem Text]
- [Symptom mit Beispielzitat]

## Aufteilungs-Vorschlag

Aus der bestehenden Seite werden N neue Seiten:

1. **[Titel]** ([Seitentyp])
   - Inhalt aus den Quellabsätzen: [Liste]
   - Verlinkung zu: [andere neue Seiten]

2. **[Titel]** ([Seitentyp])
   - Inhalt aus den Quellabsätzen: [Liste]
   - Verlinkung zu: [andere neue Seiten]

## Was wegfällt

- [Inhalte, die nur Hersteller-Doku duplizieren, werden durch Verlinkung ersetzt]

## Alternative

Statt aufzuteilen könnten wir auch [z.B. Aufklappbereiche nutzen]. Das wäre weniger eingreifend, hätte aber den Nachteil [Begründung].

## Frage

Soll ich so aufteilen, anders aufteilen, oder die Alternative umsetzen?
```

Warte auf Bestätigung, **bevor** du die einzelnen neuen Seiten erstellst.

# === DATEI: references/vorlage-anleitung.md ===

# Vorlage: Anleitung (How-to)

## Frageleitfaden (Modus A)

Stelle diese Fragen, falls noch nicht beantwortet:

1. **Was ist die Aufgabe?** Konkret, in Imperativ-Form formulierbar?
2. **Wer ist die Zielperson?** Welche Rolle, welches Vorwissen?
3. **Was muss vorher erfüllt sein?** (Zugänge, Berechtigungen, vorherige Schritte)
4. **Welche Schritte sind nötig?** Kürzeste sinnvolle Folge.
5. **Woran erkennt die Person, dass die Aufgabe erfolgreich erledigt ist?**
6. **Welche Stolpersteine gibt es für Neueinsteiger?** (kommt in Aufklappbereich)
7. **Welche Rolle ist verantwortlich** für diese Seite?

## Vorlage

```markdown
## Kurzbeschreibung

[1 bis 3 Sätze: Was erreicht diese Anleitung, für wen ist sie?]

## Voraussetzungen

* [Was muss vorher erledigt sein?]
* [Welche Zugänge / Berechtigungen sind nötig?]

## Schritte

1. [Imperativ-Schritt]
2. [Imperativ-Schritt]
3. [Imperativ-Schritt]

## Ergebnis

[Woran erkennst du, dass die Aufgabe erfolgreich erledigt ist?]

<details>
<summary>Häufige Fragen und Stolpersteine</summary>

[Optional: Was geht schief, was sollten Neue wissen?]

</details>

## Verwandte Seiten

* [Link]

## Metadaten

*Verantwortliche Rolle: [Rolle] · Letzte Aktualisierung: [JJJJ-MM-TT] · Letzte Prüfung: [JJJJ-MM-TT]*
```

## Hinweise zum Ausfüllen

* **Imperativ:** „Öffne", „Wähle", „Speichere". Nicht „Es muss geöffnet werden".
* **Ein Schritt, eine Handlung.** Keine Sammelpunkte mit drei Aktionen.
* **Vor Schritten warnen, die irreversibel sind**, mit fettgedrucktem Hinweis vor dem Schritt.
* **Aufklappbereich nur einsetzen**, wenn es echte Stolpersteine oder Begründungen gibt. Sonst weglassen.

# === DATEI: references/vorlage-prozess.md ===

# Vorlage: Prozessbeschreibung

## Frageleitfaden (Modus A)

1. **Wie heisst der Prozess?** (Substantiv, kurz)
2. **Was löst ihn aus?** (Ereignis, Frist, Antrag)
3. **Welche Rollen sind beteiligt?** (jede mit ihrer Aufgabe)
4. **Welche Schritte gibt es?** (in chronologischer Reihenfolge, mit Rollenzuordnung)
5. **Was liegt am Ende vor?** (Ergebnis, Output, Zustand)
6. **Welche Rolle ist für die Korrektheit dieser Beschreibung verantwortlich?**

## Vorlage

```markdown
## Kurzbeschreibung

[Welcher Ablauf, wann ausgelöst, mit welchem Ergebnis?]

## Auslöser

[Was startet diesen Prozess?]

## Beteiligte Rollen

* [Rolle]: [Aufgabe]

## Ablauf

1. [Schritt, welche Rolle macht was?]
2. [Schritt, welche Rolle macht was?]

## Ergebnis

[Was liegt am Ende vor?]

<details>
<summary>Hintergrund: Warum ist dieser Prozess so gestaltet?</summary>

[Optional]

</details>

## Verwandte Seiten / Tools

* [Link]

## Metadaten

*Verantwortliche Rolle: [Rolle] · Letzte Aktualisierung: [JJJJ-MM-TT] · Letzte Prüfung: [JJJJ-MM-TT]*
```

## Hinweise zum Ausfüllen

* **Rollen, nicht Personen.** „Mitgliederbetreuung", nicht „Anna".
* **Rolle pro Schritt sichtbar machen:** „Die Mitgliederbetreuung sendet das Begrüssungsmail."
* **Auslöser konkret machen:** „Wenn ein Antrag eingeht", nicht „bei Bedarf".
* **Hintergrund nur in den Aufklappbereich**, nicht in den Ablauf.

# === DATEI: references/vorlage-tool.md ===

# Vorlage: Tool-Übersicht

## Frageleitfaden (Modus A)

1. **Wie heisst das Tool?** (Schreibweise des Herstellers verwenden)
2. **Wofür nutzen wir es?** (1 bis 3 Sätze, abgegrenzt von anderen Tools)
3. **Welche Rollen brauchen Zugang?**
4. **Wie wird Zugang erteilt?** (Welche Rolle ist zuständig?)
5. **Welche Konventionen haben wir vereinbart?** (Namensschemata, Ordnerstruktur, Tags, Workflows)
6. **Wo liegt die offizielle Dokumentation?** (URL)
7. **Welche eigenen Anleitungen verweisen auf dieses Tool?**

## Vorlage

```markdown
## Kurzbeschreibung

[Wofür nutzen wir dieses Tool in der Gruppe?]

## Wer nutzt es

[Welche Rollen brauchen Zugang?]

## Zugang

[Wie bekommt man Zugang? Welche Rolle erteilt ihn?]

## Unsere Konventionen

* [Namensschema, Ordnerstruktur, Tags etc.]
* [Was ist erlaubt, was nicht?]

## Offizielle Dokumentation

* [Link zur Hersteller-Doku]
* [Link zu relevanten Tutorials]

## Anleitungen mit diesem Tool

* [Interne Links]

<details>
<summary>Warum genau dieses Tool?</summary>

[Optional: Begründung der Auswahl, Alternativen, die geprüft wurden]

</details>

## Metadaten

*Verantwortliche Rolle: [Rolle] · Letzte Aktualisierung: [JJJJ-MM-TT] · Letzte Prüfung: [JJJJ-MM-TT]*
```

## Hinweise zum Ausfüllen

* **Hersteller-Doku verlinken, nicht abschreiben.** Das ist Prinzip P2. Wenn jemand schreiben will „So funktioniert WordPress: …", lautet die richtige Antwort: „Siehe [WordPress-Dokumentation]".
* **Konventionen sind das Herzstück** dieser Seite. Hier steht, was *wir* spezifisch festgelegt haben.
* **Schreibweise konsistent**: „WordPress", nicht „Wordpress".

# === DATEI: references/vorlage-rolle.md ===

# Vorlage: Rolle / Organisationseinheit

## Frageleitfaden (Modus A)

1. **Wie heisst die Rolle?** (Funktionsbezeichnung, kein Personenname)
2. **Was umfasst die Rolle?** (1 bis 2 Sätze, prägnant)
3. **Welche Verantwortlichkeiten** hat diese Rolle?
4. **Welche Befugnisse**: Was darf diese Rolle entscheiden?
5. **Mit welchen anderen Rollen** arbeitet sie zusammen?
6. **An welche Rolle berichtet** sie, wenn das relevant ist?
7. **Welche Rolle ist für die Pflege dieser Seite zuständig?**

## Vorlage

```markdown
## Kurzbeschreibung

[1 bis 2 Sätze: Was umfasst diese Rolle?]

## Verantwortlichkeiten

* [Verantwortlichkeit]

## Befugnisse

* [Was darf diese Rolle entscheiden?]

## Schnittstellen

* Arbeitet zusammen mit: [andere Rollen]
* Berichtet an: [Rolle]

<details>
<summary>Hintergrund zur Rolle</summary>

[Optional]

</details>

## Metadaten

*Verantwortliche Rolle: [Rolle] · Letzte Aktualisierung: [JJJJ-MM-TT] · Letzte Prüfung: [JJJJ-MM-TT]*
```

## Hinweise zum Ausfüllen

* **Niemals Personennamen.** Die aktuelle Person zu einer Rolle wird an einer separaten Stelle gepflegt, nicht im Handbuch.
* **Verantwortlichkeit vs. Befugnis trennen:** Verantwortung („sorgt dafür, dass …") ist eine Pflicht; Befugnis („darf entscheiden, ob …") ist ein Recht.
* **Sparsam mit Schnittstellen**, nur die wirklich relevanten Rollen nennen.

# === DATEI: references/vorlage-konzept.md ===

# Vorlage: Hintergrund / Konzept

## Frageleitfaden (Modus A)

1. **Welche Frage soll diese Seite beantworten?** Formuliere sie als „Warum …?"-Frage.
2. **Worum geht es?** (Sachverhalt in eigenen Worten)
3. **Warum machen wir das so?** (Begründung, Abwägungen)
4. **Was bedeutet das konkret für unsere Arbeit?** (Auswirkungen, Konsequenzen)
5. **Welche Rolle ist für diese konzeptionelle Festlegung verantwortlich?**

## Vorlage

```markdown
## Kurzbeschreibung

[Welche Frage beantwortet diese Seite?]

## Worum geht es

[Erklärung]

## Warum machen wir das so

[Begründung]

## Was bedeutet das für unsere Arbeit

[Konkrete Auswirkungen]

## Verwandte Seiten

* [Link]

## Metadaten

*Verantwortliche Rolle: [Rolle] · Letzte Aktualisierung: [JJJJ-MM-TT] · Letzte Prüfung: [JJJJ-MM-TT]*
```

## Hinweise zum Ausfüllen

* **Konzeptseiten sind keine Anleitungen.** Hier stehen keine Schritte und keine Imperative, sondern Erklärungen.
* **Begründung statt Behauptung.** „Weil das die Pflege halbiert" ist besser als „Weil es besser ist".
* **Verlinkungsknotenpunkt:** Konzeptseiten sind oft das Ziel von Aufklappbereichen anderer Seiten. Halte sie deshalb klar und stabil.

# === DATEI: references/schreibregeln.md ===

# Schreibregeln

Diese Regeln gelten für **alle** Seiten des Handbuchs. Sie sind eine vereinfachte Auswahl aus der [tekom-Leitlinie „Regelbasiertes Schreiben"](https://www.tekom.de/fileadmin/tekom.de/Die_tekom/Publikationen/Leseproben/2013_RBS_Deutsch_fuer_die_TK_Leseprobe.pdf).

## S1, Aktiv statt passiv

Richtig: „Klicke auf *Speichern*."
Falsch: „Auf *Speichern* muss geklickt werden."

## S2, Kurze Sätze

Faustregel: ein Gedanke pro Satz. Sätze über 25 Wörter prüfen und meist teilen.

## S3, Imperativ in Anleitungen

Anleitungsschritte sind Befehle: „Öffne…", „Wähle…", „Speichere…".

## S4, Konkrete Wörter statt abstrakter

Richtig: „Das Formular"
Falsch: „Die entsprechende Eingabemaske"

## S5, Eine Bedeutung, ein Begriff

Verwende für dieselbe Sache immer dasselbe Wort. Nicht abwechselnd „Mitglied", „Person", „Teilnehmer:in", wenn dasselbe gemeint ist.

## S6, Anrede konsistent

Wir duzen im Handbuch durchgehend („du", kleingeschrieben).

## S7, Keine Füllwörter

Streiche „eigentlich", „grundsätzlich", „im Prinzip", „natürlich".

## S8, Gendergerecht und lesbar

Doppelpunkt („Mitarbeiter:innen") oder geschlechtsneutrale Formulierungen („das Team", „die Mitglieder"). Konsistent über alle Seiten.

## Terminologie

* **Tool-Namen** in der Schreibweise des Herstellers: „WordPress", „GitHub", „LibreOffice".
* **Begriffe aus dem Glossar** beim ersten Vorkommen verlinken.
* **Konsistenz vor Eleganz:** Wenn zwei Formulierungen gleich gut wären, gewinnt die bereits verwendete.

# === DATEI: references/markdown-konventionen.md ===

# Markdown-Konventionen

Diese Konventionen sind für die Veröffentlichung in WordPress optimiert.

## Überschriften

* **Erste Überschrift im Inhalt ist `##`** (zweite Ebene). WordPress setzt die `#`/H1 automatisch aus dem Seitentitel; eine zweite H1 würde die Seitenstruktur und SEO/Barrierefreiheit brechen.
* `##` für Hauptabschnitte, `###` für Unterabschnitte.
* Maximal vier Ebenen (`####`); tiefer wird unübersichtlich.

## Aufklappbereich „Weitere Informationen"

```html
<details>
<summary>Aussagekräftiger Titel des Aufklappbereichs</summary>

Inhalt des Aufklappbereichs in normalem Markdown.

</details>
```

**Regeln:**

* Maximal eine Ebene (keine verschachtelten `<details>`).
* Aussagekräftiger Titel, nicht „Mehr Infos".
* Keine kritischen Inhalte, der Pflichtweg muss ohne Aufklappen funktionieren.
* Sparsam, mehr als zwei bis drei pro Seite ist ein Aufteilungs-Signal.

## Listen

* **Aufzählungen** mit `*` (Sternchen, einheitlich).
* **Nummerierte Listen** nur, wenn die Reihenfolge zwingend ist (Schritte).
* Pro Listenpunkt ein Gedanke.

## Links

* **Interne Links**: relativer Pfad oder Anker.
* **Externe Links** (Hersteller-Dokus, Quellen): voller URL.
* **Linktext beschreibt das Ziel:** richtig: „[Diátaxis-Framework](https://diataxis.fr/)"; falsch: „[hier klicken](https://...)".

## Code

* Inline mit Backticks: `` `Befehl` ``.
* Codeblöcke mit Sprachangabe für Syntax-Highlighting.

## Hervorhebungen

* **Fett** (`**...**`) für wichtige Begriffe und UI-Elemente.
* *Kursiv* (`*...*`) für Eigennamen, Zitate, Bildschirmbeschriftungen.
* Sparsam einsetzen.

## Tabellen

Nur bei vergleichendem oder mehrdimensionalem Inhalt. Sonst Listen.

## Metadaten am Seitenende

Pflichtformat:

```markdown
## Metadaten

*Verantwortliche Rolle: [Rolle] · Letzte Aktualisierung: [JJJJ-MM-TT] · Letzte Prüfung: [JJJJ-MM-TT]*
```

* **Verantwortliche Rolle**, nie ein Personenname.
* **Letzte Aktualisierung**: Datum der letzten inhaltlichen Änderung.
* **Letzte Prüfung**: Datum, an dem zuletzt aktiv auf Korrektheit geprüft wurde, auch wenn keine Änderung nötig war.

# === DATEI: references/review-checkliste.md ===

# Review-Checkliste

Gehe diese Checkliste systematisch durch. Bei jedem Punkt: prüfen, Befund festhalten, ggf. Korrekturvorschlag formulieren.

## Vorab-Check: Mischform?

* [ ] Die Seite hat **einen** klar erkennbaren Hauptzweck (kein Mischmasch verschiedener Seitentypen). Falls Mischform: in den Befund aufnehmen und auf Workflow W3 (Aufteilen) hinweisen.

## Inhalt

* [ ] Der **Seitentyp** ist klar erkennbar (Anleitung / Prozess / Übersicht / Rolle / Hintergrund).
* [ ] Die Information ist **fachlich korrekt** und **aktuell**.
* [ ] Externe Tool-Inhalte sind **verlinkt, nicht kopiert**.

## Struktur

* [ ] **Erste Überschrift im Inhalt ist `##`**, keine `#` im Inhalt.
* [ ] **Kurzbeschreibung** beantwortet „Was?" und „Für wen?".
* [ ] **Aufklappbereiche** enthalten nur ergänzende, keine kritischen Inhalte.
* [ ] **Aufklappbereiche** sind nicht verschachtelt.
* [ ] **Metadaten** (verantwortliche Rolle, Datum letzte Aktualisierung, Datum letzte Prüfung) sind gesetzt.
* [ ] **Verantwortlichkeit** ist über eine **Rolle** zugewiesen, nicht über eine Person.

## Sprache

* [ ] Aktiv-Konstruktion und Imperativ verwendet (wo zutreffend).
* [ ] Sätze sind kurz und klar.
* [ ] Begriffe werden konsistent verwendet (kein Synonymwechsel für dasselbe Konzept).
* [ ] Keine Füllwörter, keine doppelten Verneinungen.
* [ ] Tool-Namen in Hersteller-Schreibweise.

## Auffindbarkeit

* [ ] Die Seite ist mit verwandten Seiten **verlinkt**.
* [ ] Begriffe, die im Glossar stehen, sind beim ersten Vorkommen verlinkt.
* [ ] Linktexte beschreiben das Ziel, kein „hier klicken".

## Befund-Format

Liefere Funde in dieser Form:

> **Abschnitt:** [Name oder Position]
> **Befund:** [was beobachtet]
> **Vorschlag:** [konkrete Korrektur]

# === Spätere Installation ===

Wenn dieser Skill-Entwurf getestet und für gut befunden ist, wird er installiert, indem die obigen Abschnitte in folgende Dateistruktur aufgeteilt werden:

```
handbuch-autor/
├── SKILL.md                       (Abschnitt "DATEI: SKILL.md")
└── references/
    ├── inhaltstypen.md            (Abschnitt "DATEI: references/inhaltstypen.md")
    ├── aufteilen.md
    ├── vorlage-anleitung.md
    ├── vorlage-prozess.md
    ├── vorlage-tool.md
    ├── vorlage-rolle.md
    ├── vorlage-konzept.md
    ├── schreibregeln.md
    ├── markdown-konventionen.md
    └── review-checkliste.md
```

Das Aufteilen kann manuell erfolgen oder, falls gewünscht, automatisiert in einem späteren Schritt.
