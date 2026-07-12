# So legst du eine Handbuch-Seite an

## Kurzbeschreibung

Diese Anleitung zeigt, wie du eine neue Seite im Handbuch anlegst, einordnest und veröffentlichst. Sie richtet sich an alle Teammitglieder, die Inhalte beisteuern.

<details>
<summary>Konzept</summary>

Eine Handbuch-Seite ist kein normaler WordPress-Beitrag, sondern gehört zur eigenen Inhaltsart **Handbuch**. Sie bekommt ihren Platz im Menü über die Eltern-Seite, nicht über eine Menü-Pflege von Hand. Der empfohlene Weg führt über den Markdown-Import: Entwurf im Repo schreiben, importieren, prüfen, veröffentlichen. Begriffe wie Seitentyp oder Themengebiet erklärt die [Übersicht zur Handbuch-Applikation](uebersicht-handbuch-applikation.md).

</details>

<details>
<summary>Voraussetzungen</summary>

* WordPress-Konto mit Schreibrecht für das Handbuch.
* Fertiger Entwurf nach der passenden Vorlage der *Anleitung zur Erstellung des Team-Handbuchs*, mit Transport-Block.
* Bekannte Eltern-Seite und verantwortliche Rolle (stehen im Transport-Block).

</details>

## Schritte

1. Öffne im Adminbereich **Handbuch → Markdown-Import**.
2. Trage den **Dateinamen ohne .md** ein; er wird der Slug der Seite.
3. Füge den **kompletten Markdown-Entwurf** ein, mit `# Titel` und Transport-Block, unverändert.
4. Klicke auf **Als Entwurf importieren**; Inhalt, Aufklappbereiche und alle Felder werden automatisch gesetzt.
5. Lies allfällige Warnhinweise (z.B. fehlende Eltern-Seite) und kontrolliere den Entwurf im Editor.
6. Klicke auf **Veröffentlichen**.
7. Nach der letzten Seite eines Bereichs: Öffne **Handbuch → Wartung** und klicke auf **.md-Links jetzt automatisch konvertieren**.

![](handbuch-seiten-anlegen-schritte.png)

## Ergebnis

Die Seite ist über das Handbuch-Menü an der gewählten Stelle erreichbar, erscheint als Karte auf der Übersichtsseite und zeigt am Seitenende automatisch die Metadaten-Fußzeile. Menü, Filter und Suche haben sich ohne weiteres Zutun aktualisiert.

<details>
<summary>Häufige Fragen und Stolpersteine</summary>

Der Import bricht bei einem bereits vergebenen Slug ab; lösche die alte Seite endgültig oder wähle einen anderen Dateinamen. Importierst du ein Kind vor seiner Eltern-Seite, hängt es zunächst auf der obersten Menüebene; trage die Eltern-Seite nach deren Import unter Seiten-Attribute nach. Interne Links bleiben bis zur Konvertierung auf die Entwurfsdateien gerichtet; die Seite ist bis dahin in der Handbuch-Liste markiert.

</details>

## Verwandte Seiten

* [Übersicht: Handbuch-Applikation](uebersicht-handbuch-applikation.md)
* [So prüfst du eine Seite auf Aktualität](seite-pruefen.md)

---

## Transport-Metadaten (beim Erfassen in Felder übertragen, dann diesen Block löschen)

* Seitentyp: Anleitung
* Verantwortliche Rolle: [ANNAHME: Handbuch-Redaktion]
* Themengebiet: [ANNAHME: Technik]
* Zielgruppe: Inhalts-Ersteller:innen
* Eltern-Seite: Übersicht: Handbuch-Applikation
* Reihenfolge: 10
* Textauszug: Diese Anleitung zeigt, wie du eine neue Seite im Handbuch anlegst, einordnest und veröffentlichst.
* Letzte Aktualisierung: [JJJJ-MM-TT]
* Letzte Prüfung: [JJJJ-MM-TT]
* Prüfintervall: 180
