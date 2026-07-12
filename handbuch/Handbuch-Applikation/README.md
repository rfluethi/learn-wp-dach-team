# Handbuch-Applikation

## Kurzbeschreibung

Die Handbuch-Applikation ist der Bereich unserer WordPress-Installation, in dem das Team-Handbuch geschrieben, gepflegt und gelesen wird. Diese Seite beschreibt, was die Applikation kann, wer sie nutzt und welche Konventionen gelten.

<details>
<summary>Konzept</summary>

Das Handbuch ist eine eigene Inhaltsart in WordPress, getrennt von normalen Seiten und Beiträgen. Du erreichst es im Adminbereich über den Menüpunkt **Handbuch** (Buch-Symbol). Alles, was du dort anlegst, erscheint automatisch im Handbuch-Menü und auf der Übersichtsseite; du musst nichts von Hand verlinken.

</details>

## Wer nutzt es

* **Alle Teammitglieder** lesen das Handbuch und geben Feedback („War diese Seite hilfreich?").
* **Autor:innen** legen Seiten an und pflegen sie.
* **Inhaltsverantwortliche Rollen** prüfen ihre Seiten regelmäßig und geben sie frei.
* **Handbuch-Redaktion** überwacht die Wartungsübersicht und wertet Feedback aus.

## Zugang

Das Handbuch ist intern: Lesen und Schreiben setzen ein Konto auf unserer WordPress-Installation voraus. Zugänge erteilt die Technik-Verantwortung.

## Unsere Konventionen

* **Jede Seite hat einen Seitentyp** (Anleitung, Prozessbeschreibung, Tool-Übersicht, Rolle/Organisation, Hintergrund/Konzept, FAQ) und wird nach der zugehörigen Vorlage geschrieben.
* **Vier Schlagwort-Gruppen** pro Seite: Seitentyp, Themengebiet, Verantwortliche Rolle, Zielgruppe. Sie speisen Filter und Suche der Übersicht.
* **Das Menü entsteht automatisch** aus Eltern-Seite und Reihenfolge in den Seiten-Attributen; Details: [Warum das Menü aus der Seiten-Hierarchie entsteht](warum-menue-aus-seiten-hierarchie.md).
* **Metadaten leben in Feldern**, nie im Seiteninhalt; die Fußzeile mit Erstellt/Aktualisiert/Geprüft/Rolle rendert die Applikation automatisch.
* **Erfassung über den Markdown-Import** (Handbuch → Markdown-Import): Entwürfe entstehen im Repo und werden importiert, nicht von Hand eingefügt.
* **Verbindlich für alle Inhalte** ist das [Regelwerk Handbuch-Erstellung](../Handbuch-Erstellung/README.md); der Skill **handbuch-autor** setzt es beim Schreiben mit KI-Unterstützung um.

## Offizielle Dokumentation

* [WordPress-Benutzerdokumentation](https://wordpress.org/documentation/) für die Grundbedienung des Block-Editors.
* Für die Handbuch-spezifischen Funktionen ist **dieses Handbuch** die Dokumentation (die Applikation ist eine Eigenentwicklung).

## Seiten in diesem Bereich

| Datei | Seitentyp | Beschreibung |
|---|---|---|
| [handbuch-seite-anlegen.md](handbuch-seite-anlegen.md) | Anleitung | Neue Seite anlegen: Inhalt, Menüplatz, Schlagworte, Auszug, Aktualitäts-Felder. |
| [seite-pruefen.md](seite-pruefen.md) | Anleitung | Seite inhaltlich prüfen und die Prüfung festhalten. |
| [wartung-des-handbuchs.md](wartung-des-handbuchs.md) | Prozessbeschreibung | Fällige Prüfungen, Eskalation UNGEPRÜFT, Verteilung in der Sitzung, Feedback-Auswertung. |
| [warum-menue-aus-seiten-hierarchie.md](warum-menue-aus-seiten-hierarchie.md) | Hintergrund/Konzept | Warum das Menü aus dem Seitenbaum entsteht und Themen nur Filter sind. |
| [haeufige-fragen-handbuch.md](haeufige-fragen-handbuch.md) | FAQ | Wegweiser-Fragen zu den obigen Seiten. |

<details>
<summary>Warum genau diese Lösung?</summary>

Wir haben das Handbuch als eigene Inhaltsart in WordPress gebaut, statt ein Wiki oder ein zweites System zu betreiben: WordPress ist bereits unsere zentrale Plattform, das Team kennt den Editor, und die Single Source of Truth bleibt an einem Ort. Die Hintergründe stehen in den Konzeptdokumenten des Projekts Handbuch-Training-DACH.

</details>

---

## Transport-Metadaten (beim Erfassen in Felder übertragen, dann diesen Block löschen)

* Seitentyp: Bereichs-Übersicht
* Slug: handbuch-applikation
* Verantwortliche Rolle: Handbuch-Redaktion
* Themengebiet: Technik
* Zielgruppe: Alle Mitglieder
* Eltern-Seite: oberste Ebene
* Reihenfolge: 10
* Textauszug: Die Handbuch-Applikation ist der Bereich unserer WordPress-Installation, in dem das Team-Handbuch geschrieben, gepflegt und gelesen wird.
* Letzte Aktualisierung: 2026-07-12
* Letzte Prüfung: [JJJJ-MM-TT]
* Prüfintervall: 90
