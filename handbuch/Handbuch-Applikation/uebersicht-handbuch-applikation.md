# Übersicht: Handbuch-Applikation

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

Das Handbuch ist intern: Lesen und Schreiben setzen ein Konto auf unserer WordPress-Installation voraus. Zugänge erteilt die [ANNAHME: Technik-Verantwortung].

## Unsere Konventionen

* **Jede Seite hat einen Seitentyp** (Anleitung, Prozessbeschreibung, Tool-Übersicht, Rolle/Organisation, Hintergrund/Konzept, FAQ) und wird nach der zugehörigen Vorlage geschrieben.
* **Vier Schlagwort-Gruppen** pro Seite: Seitentyp, Themengebiet, Verantwortliche Rolle, Zielgruppe. Sie speisen Filter und Suche der Übersicht.
* **Das Menü entsteht automatisch** aus Eltern-Seite und Reihenfolge in den Seiten-Attributen; Details: [Warum das Menü aus der Seiten-Hierarchie entsteht](warum-menue-aus-seiten-hierarchie.md).
* **Metadaten leben in Feldern**, nie im Seiteninhalt; die Fußzeile mit Erstellt/Aktualisiert/Geprüft/Rolle rendert die Applikation automatisch.
* **Erfassung über den Markdown-Import** (Handbuch → Markdown-Import): Entwürfe entstehen im Repo und werden importiert, nicht von Hand eingefügt.
* **Verbindliches Regelwerk** für alle Inhalte ist die *Anleitung zur Erstellung des Team-Handbuchs*; der Skill **handbuch-autor** setzt sie beim Schreiben mit KI-Unterstützung um.

## Offizielle Dokumentation

* [WordPress-Benutzerdokumentation](https://wordpress.org/documentation/) für die Grundbedienung des Block-Editors.
* Für die Handbuch-spezifischen Funktionen ist **dieses Handbuch** die Dokumentation (die Applikation ist eine Eigenentwicklung).

## Anleitungen mit diesem Tool

* [So legst du eine Handbuch-Seite an](handbuch-seite-anlegen.md)
* [So prüfst du eine Seite auf Aktualität](seite-pruefen.md)
* [Wartung des Handbuchs](wartung-des-handbuchs.md)
* [Häufige Fragen zur Handbuch-Applikation](haeufige-fragen-handbuch.md)

<details>
<summary>Warum genau diese Lösung?</summary>

Wir haben das Handbuch als eigene Inhaltsart in WordPress gebaut, statt ein Wiki oder ein zweites System zu betreiben: WordPress ist bereits unsere zentrale Plattform, das Team kennt den Editor, und die Single Source of Truth bleibt an einem Ort. Die Hintergründe stehen in den Konzeptdokumenten des Projekts Handbuch-Training-DACH.

</details>

---

## Transport-Metadaten (beim Erfassen in Felder übertragen, dann diesen Block löschen)

* Seitentyp: Tool-Übersicht
* Verantwortliche Rolle: [ANNAHME: Handbuch-Redaktion]
* Themengebiet: [ANNAHME: Technik]
* Zielgruppe: Alle Mitglieder
* Eltern-Seite: oberste Ebene
* Reihenfolge: 10
* Textauszug: Die Handbuch-Applikation ist der Bereich unserer WordPress-Installation, in dem das Team-Handbuch geschrieben, gepflegt und gelesen wird.
* Letzte Aktualisierung: [JJJJ-MM-TT]
* Letzte Prüfung: [JJJJ-MM-TT]
* Prüfintervall: 90
