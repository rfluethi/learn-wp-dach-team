# Markdown-Konventionen

Markdown ist bei uns **Entwurfsformat**, WordPress (Block-Editor) ist die Single Source of Truth. Diese Konventionen sorgen dafür, dass ein Entwurf verlustfrei in den Block-Editor übertragen werden kann (Anleitung, Kapitel 13).

## Dateiname = WordPress-Slug (Pflicht)

Der Dateiname eines Entwurfs ist der spätere **WordPress-Slug** der Seite: Kleinbuchstaben, Bindestriche, keine Umlaute, keine Leerzeichen (z.B. `handbuch-seite-anlegen.md` → Seite mit Slug `handbuch-seite-anlegen`). Dadurch ist jeder interne Link mechanisch und eindeutig in einen WordPress-Link übersetzbar; nichts muss interpretiert werden.

## Überschriften

* **Erste Überschrift im Inhalt ist `##`** (H2). WordPress setzt die H1 automatisch aus dem Seitentitel; eine zweite H1 bricht Seitenstruktur und Barrierefreiheit.
* `##` für Hauptabschnitte, `###` für Unterabschnitte, maximal vier Ebenen.

## Aufklappbereiche

```html
<details>
<summary>Aussagekräftiger Titel des Aufklappbereichs</summary>

Inhalt in normalem Markdown.

</details>
```

**Regeln:**

* Maximal eine Ebene, keine Verschachtelung.
* Aussagekräftiger Titel, nicht „Mehr Infos".
* Keine kritischen Inhalte; der Pflichtweg funktioniert ohne Aufklappen.
* Sparsam: mehr als zwei bis drei pro Seite ist ein Aufteilungs-Signal.
* **Standard-Aufklappbereich „Für neue Mitglieder":** fester Titel, genau so geschrieben; nur ergänzender Kontext, ein bis zwei Absätze, höchstens einer pro Abschnitt.
* Beim Übertrag nach WordPress wird jedes `<details>` ein **Details-Block** (Kernblock ab WordPress 6.3).

## Listen, Links, Code, Hervorhebungen, Tabellen

* Aufzählungen mit `*`; nummerierte Listen nur bei zwingender Reihenfolge; pro Punkt ein Gedanke.
* **Interne Links in Entwürfen: relativer `.md`-Link auf die Zieldatei** (funktioniert auf GitHub). Beim Erfassen in WordPress werden sie anhand der Slug-Konvention auf die Zielseiten umgestellt (siehe `wordpress-erfassung.md`); ein `.md`-Link in einer veröffentlichten Seite ist immer ein Fehler.
* Externe Links mit vollem URL; Linktext beschreibt das Ziel, kein „hier klicken".
* Inline-Code mit Backticks, Codeblöcke mit Sprachangabe.
* **Fett** für wichtige Begriffe und UI-Elemente, *kursiv* für Eigennamen und Bildschirmbeschriftungen, beides sparsam.
* Tabellen nur bei vergleichendem oder mehrdimensionalem Inhalt.

## Transport-Block am Ende des Entwurfs (Pflicht)

In WordPress leben Metadaten **ausschließlich in Feldern** (Meta-Box, Taxonomien, Seiten-Attribute, Textauszug); das Template zeigt sie automatisch an. Damit beim Entwurf nichts verloren geht, endet jeder Markdown-Entwurf mit einem klar markierten **Transport-Block**. Er wird bei der Erfassung in die Felder übertragen und **aus dem Inhalt gelöscht** (siehe `wordpress-erfassung.md`).

```markdown
---

## Transport-Metadaten (beim Erfassen in Felder übertragen, dann diesen Block löschen)

* Seitentyp: [Anleitung|Prozessbeschreibung|Tool-Übersicht|Rolle/Organisation|Hintergrund/Konzept|FAQ]
* Verantwortliche Rolle: [Rolle]
* Themengebiet: [Begriff]
* Zielgruppe: [Alle Mitglieder|Inhalts-Ersteller:innen|Organisation/Koordination|Technik; Mehrfachnennung möglich]
* Eltern-Seite: [Titel oder „oberste Ebene"]
* Reihenfolge: [Zahl]
* Textauszug: [wortgleich der erste Satz der Kurzbeschreibung]
* Letzte Aktualisierung: [JJJJ-MM-TT]
* Letzte Prüfung: [JJJJ-MM-TT]
* Prüfintervall: [Tage; Startwerte: Tool 90, Anleitung/Prozess 180, sonst 365]
```

**Regeln:**

* Der Transport-Block ist **kein Seiteninhalt**. Er darf nie mitveröffentlicht werden.
* Unbekannte Werte bleiben Platzhalter; nichts raten (insbesondere Rolle, Eltern-Seite, Reihenfolge).
* **Textauszug = erster Satz der Kurzbeschreibung, wortgleich.** So gibt es keine zwei driftenden Zusammenfassungen; wer die Kurzbeschreibung ändert, zieht den Auszug nach.
* **Zielgruppe ist funktionsbasiert** (Entscheid 2026-07-05): Für wen ist die Seite? „Alle Mitglieder" nur, wenn wirklich alle die Seite brauchen; sonst die konkrete Gruppe. Der Lesemodus Onboarding/Nachschlagen ist **kein** Schlagwort; ihn löst der Aufklappbereich „Für neue Mitglieder".
* Ein Glossar-Abschnitt (falls vorhanden) steht **vor** dem Transport-Block und ist echter Seiteninhalt.
