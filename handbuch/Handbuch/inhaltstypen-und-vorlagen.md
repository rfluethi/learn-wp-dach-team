## Kurzbeschreibung

Diese Seite legt fest, welche fünf [Seitentypen](glossar.md) das Handbuch kennt, wie eine Seite aufgebaut ist, wie wir Aufklappbereiche einsetzen und welche Vorlagen pro Inhaltstyp gelten. Sie richtet sich an Autor:innen und Reviewer:innen.

## Wer nutzt es

Alle Personen, die eine neue Seite anlegen oder eine bestehende überarbeiten. Pflichtlektüre vor jeder Seitenerstellung.

## Die fünf Seitentypen

Wir orientieren uns am [Diátaxis-Framework](https://diataxis.fr/), das vier Inhaltstypen unterscheidet. Für unser Handbuch passen wir das auf folgende fünf praktische Seitentypen an:

| Seitentyp | Diátaxis-Typ | Zweck | Typischer Titel |
|---|---|---|---|
| **Anleitung** | How-to-Guide | Aufgabe Schritt für Schritt erledigen | „So legst du eine neue Mitgliederliste an" |
| **Prozessbeschreibung** | How-to-Guide | Wiederkehrenden Ablauf dokumentieren | „Aufnahme eines neuen Mitglieds" |
| **Tool-Übersicht** | Reference | Was wir nutzen, wofür, mit Link zur Hersteller-Doku | „Übersicht: WordPress" |
| **Rollen- und Organisationsbeschreibung** | Reference | Struktur der Gruppe, Verantwortlichkeiten | „Rollen im Team" |
| **Hintergrund / Konzept** | Explanation | Warum-Fragen, Zusammenhänge | „Warum wir Markdown verwenden" |

**Regel:** Lege vor dem Schreiben einer Seite den Seitentyp fest. Steht er nicht eindeutig fest, ist die Seite vermutlich eine Mischform; teile sie dann auf.

<details>
<summary>Weiterführend: Diátaxis und verwandte Standards</summary>

Eine kompakte Erklärung der vier Diátaxis-Typen findet sich unter [diataxis.fr/start-here](https://diataxis.fr/start-here/). Auch der internationale Standard [ISO/IEC/IEEE 26514:2022](https://www.iso.org/standard/72657.html) regelt Struktur und Format von Nutzerdokumentation.

Die Rollen- und Organisationsbeschreibung ordnen wir bewusst ausschliesslich dem Diátaxis-Typ Reference zu, obwohl sie oft auch erklärende Anteile enthält. Diese Anteile gehören in den Aufklappbereich der jeweiligen Rollenseite.

</details>

## Aufbau einer Seite

Jede Seite folgt dieser Grundstruktur. Pflichtelemente sind als solche gekennzeichnet.

```
Pflicht: Titel (klar, aufgabenorientiert)
Pflicht: Kurzbeschreibung (1 bis 3 Sätze: was und für wen)
Pflicht: Hauptinhalt (abhängig vom Seitentyp, siehe Vorlagen unten)
Optional: Aufklappbereich(e) „Weitere Informationen"
Optional: Verwandte Seiten / Links
Pflicht: Metadaten am Seitenende:
   * Verantwortliche Rolle
   * Letzte Aktualisierung (Datum)
   * Letzte Prüfung (Datum)
```

**Begründung der Pflichtelemente:**
Titel und Kurzbeschreibung sichern die Auffindbarkeit. Die Metadaten am Ende setzen Prinzip P6 („Aktualität sichtbar") um. „Letzte Aktualisierung" zeigt, welche Version des Inhalts vorliegt. „Letzte Prüfung" zeigt, wann wir die Inhalte zuletzt aktiv auf Korrektheit geprüft haben, auch wenn dabei keine Änderung nötig war.

## Aufklappbereiche „Weitere Informationen"

Aufklappbereiche sind unser zentrales Werkzeug, um beide Zielgruppen mit **einem** Dokument zu bedienen. Sie folgen dem Prinzip [Progressive Disclosure](https://www.nngroup.com/articles/progressive-disclosure/) (Nielsen Norman Group).

### Was gehört in den Aufklappbereich?

**Geeignet:**

* Hintergrund und Begründungen („Warum machen wir das so?")
* Beispiele und Fallstricke für Neueinsteiger
* Historischer Kontext, frühere Lösungen
* Vertiefende Erklärungen, die für die Aufgabe selbst nicht nötig sind

**Nicht geeignet:**

* Pflichtschritte einer Anleitung
* Sicherheits- oder Compliance-relevante Hinweise
* Informationen, die ein erfahrenes Mitglied trotzdem braucht

### Regeln für Aufklappbereiche

1. **Maximal eine Ebene.** Keine verschachtelten Aufklappbereiche. Wer drei Ebenen tief klicken muss, findet nichts mehr (vgl. [GitLab Pajamas Design System](https://design.gitlab.com/patterns/progressive-disclosure/)).
2. **Aussagekräftiger Titel.** Nicht „Mehr Infos", sondern z.B. „Warum nutzen wir genau dieses Tool?".
3. **Keine kritischen Inhalte.** Wer nicht aufklappt, muss die Aufgabe trotzdem korrekt erledigen können.
4. **Sparsam einsetzen.** Mehr als zwei bis drei Aufklappbereiche pro Seite sind ein Hinweis darauf, dass wir die Seite besser teilen sollten.

Die Markdown-Syntax dafür steht in [Schreibregeln und Markdown-Konventionen](schreibregeln-und-markdown.md).

## Vorlagen pro Inhaltstyp

Diese Vorlagen kannst du kopieren und ausfüllen. Sie beginnen jeweils mit `##`, da WordPress den Seitentitel als `#` (H1) automatisch setzt. Eine zweite H1 im Inhalt würde die Seitenstruktur brechen.

### Vorlage A, Anleitung (How-to)

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

### Vorlage B, Prozessbeschreibung

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

### Vorlage C, Tool-Übersicht

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

### Vorlage D, Rolle / Organisationseinheit

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

### Vorlage E, Hintergrund / Konzept

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

## Verwandte Seiten

* [Regelwerk-Übersicht](WordPress-Training-Team-DACH/GitHub-Repo/learn-wp-dach-team/handbuch/Handbuch/README.md)
* [Leitprinzipien](leitprinzipien.md) – die Grundsätze hinter den Seitentypen
* [Schreibregeln und Markdown-Konventionen](schreibregeln-und-markdown.md) – Sprache und Formatierung beim Ausfüllen der Vorlagen
* [Erstellungs- und Pflegeprozess](erstellungs-und-pflegeprozess.md) – wie es nach dem Entwurf weitergeht
* [Glossar](glossar.md)

## Metadaten

*Verantwortliche Rolle: GitHub-Spezialist · Letzte Aktualisierung: 2026-05-03 · Letzte Prüfung: 2026-05-03*
