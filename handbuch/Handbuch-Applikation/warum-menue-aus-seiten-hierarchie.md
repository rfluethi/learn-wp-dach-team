# Warum das Menü aus der Seiten-Hierarchie entsteht

## Kurzbeschreibung

Diese Seite erklärt, warum das Handbuch-Menü automatisch aus Eltern-Seite und Reihenfolge entsteht und warum die Themengebiete bewusst kein Menü sind.

## Worum geht es

Jede Handbuch-Seite hat in den Seiten-Attributen eine Eltern-Seite und eine Reihenfolge-Zahl. Aus diesem Seitenbaum erzeugt die Applikation das Navigationsmenü von selbst und aktualisiert es bei jedem Veröffentlichen, Ändern oder Löschen. Die Übersichtsseite steht dabei immer zuoberst. Die Themengebiete (zum Beispiel Organisation, Technik) sind davon getrennt: Sie sind reine Schlagworte für Filter und Suche auf der Übersichtsseite.

## Warum machen wir das so

Ein von Hand gepflegtes Menü skaliert nicht: Bei einem wachsenden Handbuch müsste jede neue Seite zusätzlich in einer Menüverwaltung eingehängt werden, und vergessene Einträge fielen erst spät auf. Der Seitenbaum dagegen wird beim Anlegen ohnehin gepflegt, das Menü kann daraus nie veralten. Menü und Themen sind getrennte Sichten, weil eine Seite in genau einen Menü-Ast gehört, aber mehreren Themen zugeordnet sein kann; ein Themen-Menü würde beides vermischen und Seiten mehrfach oder gar nicht zeigen.

## Was bedeutet das für unsere Arbeit

Beim Anlegen einer Seite entscheidest du zwei Dinge getrennt: **Wo im Baum** steht die Seite (Eltern-Seite, Reihenfolge) und **welche Themen** sie berührt (Schlagworte). Das Menü musst du nie anfassen; wenn eine Seite am falschen Ort erscheint, korrigierst du ihre Seiten-Attribute, nicht das Menü.

## Verwandte Seiten

* [So legst du eine Handbuch-Seite an](handbuch-seite-anlegen.md)
* [Handbuch-Applikation](README.md) – Startseite des Bereichs

## Transport-Metadaten (beim Erfassen in Felder übertragen, dann diesen Block löschen)

* Seitentyp: Hintergrund/Konzept
* Verantwortliche Rolle: Handbuch-Redaktion
* Themengebiet: Technik
* Zielgruppe: Inhalts-Ersteller:innen
* Eltern-Seite: Handbuch-Applikation
* Reihenfolge: 40
* Textauszug: Diese Seite erklärt, warum das Handbuch-Menü automatisch aus Eltern-Seite und Reihenfolge entsteht und warum die Themengebiete bewusst kein Menü sind.
* Letzte Aktualisierung: [JJJJ-MM-TT]
* Letzte Prüfung: [JJJJ-MM-TT]
* Prüfintervall: 365
