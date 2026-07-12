# Vorlage: Anleitung (How-to)

**Gestaltungsregel (Entscheid 2026-07-05):** Auf Anleitungs-Seiten sind nur **Schritte** und **Ergebnis** offen sichtbar; Voraussetzungen, Konzept-Kontext und Stolpersteine stehen in zugeklappten Aufklappbereichen. Wer die Aufgabe kennt, sieht sofort die Schritte; alle anderen klappen auf.

## Frageleitfaden (Modus A)

1. **Was ist die Aufgabe?** Konkret, in Imperativ-Form formulierbar?
2. **Wer ist die Zielperson?** Welche Rolle, welches Vorwissen?
3. **Was muss vorher erfüllt sein?** (Zugänge, Berechtigungen, vorherige Schritte)
4. **Welche Schritte sind nötig?** Kürzeste sinnvolle Folge. Kommt mehr als eine Rolle vor, ist es eine Prozessbeschreibung (`vorlage-prozess.md`).
5. **Woran erkennt die Person den Erfolg?**
6. **Welcher Konzept-Kontext hilft beim Verstehen?** (Aufklappbereich «Konzept»; für reinen Neueinsteiger-Kontext stattdessen «Für neue Mitglieder»)
7. **Welche Stolpersteine gibt es?** (Aufklappbereich)
8. **Welche Begriffe brauchen einen Glossar-Eintrag?**
9. **Welche Rolle ist verantwortlich?** Welche Eltern-Seite, welches Themengebiet? (Transport-Block)

## Vorlage

```markdown
## Kurzbeschreibung

[1 bis 3 Sätze: Was erreicht diese Anleitung, für wen ist sie?]

<details>
<summary>Konzept</summary>

[Optional: Wie hängt diese Aufgabe mit dem Gesamtsystem zusammen? Bei reinem
Neueinsteiger-Kontext stattdessen den festen Titel «Für neue Mitglieder» verwenden.]

</details>

<details>
<summary>Voraussetzungen</summary>

* [Was muss vorher erledigt sein?]
* [Welche Zugänge / Berechtigungen sind nötig?]

</details>

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
```

Danach den **Transport-Block** aus `markdown-konventionen.md` anhängen.

## Hinweise zum Ausfüllen

* **Imperativ:** „Öffne", „Wähle", „Speichere". Nicht „Es muss geöffnet werden".
* **Ein Schritt, eine Handlung.** Keine Sammelpunkte mit drei Aktionen.
* **Vor irreversiblen Schritten warnen**, mit fettem Hinweis **vor** dem Schritt im offenen Teil (nie im Aufklappbereich).
* **Aufklappbereich-Titel:** «Voraussetzungen» und «Häufige Fragen und Stolpersteine» sind Standard; für Kontext «Konzept» oder der feste Titel «Für neue Mitglieder», je nachdem, ob es Systemzusammenhang oder Neueinsteiger-Kontext ist.
* **Aufklappbereiche nur bei echtem Inhalt** einsetzen, sonst weglassen.
