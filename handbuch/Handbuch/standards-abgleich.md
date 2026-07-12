# Standards-Abgleich: Wo wir Normen folgen und wo wir bewusst abweichen

> **Zweck:** Dieses Dokument gleicht unser Handbuch-Konzept (Anleitung v1.4, Skill handbuch-autor) mit den einschlägigen Standards ab. Pro Standard steht, was er fordert, was wir übernehmen und wo wir **begründet abweichen**. Es ist ein Hintergrunddokument; der Skill lädt es nicht zur Laufzeit.
>
> **Stand:** 2026-07-05 · Verantwortliche Rolle: Handbuch-Redaktion

## Einordnung

Unser Handbuch ist ein **internes Organisations- und Arbeitshandbuch** eines kleinen Teams (Tools, Prozesse, Rollen), kein Produkthandbuch mit Sicherheitsrelevanz und kein zertifiziertes Managementsystem. Die Standards sind darum Steinbruch, nicht Pflichtenheft: Wir übernehmen Prinzipien, die unsere Qualität heben, und lassen Formalismus weg, der auf Zertifizierung oder Produkthaftung zielt.

## Technische Dokumentation

### IEC/IEEE 82079-1:2019 (Nutzungsinformation, Grundnorm)

**Fordert u.a.:** Zielgruppenanalyse, Informationsarten trennen (instruktiv/konzeptionell/referenziell), Minimalismus (nur handlungs- oder entscheidungsrelevante Information), Verständlichkeit, definierte Erstellungs- und Prüfprozesse, qualifizierte Ersteller, Sicherheits- und Warnhinweise.

**Übernommen:** Trennung der Informationsarten (über Diátaxis, strenger als die Norm), Zielgruppenanalyse (zwei definierte Zielgruppen mit Progressive Disclosure), Minimalismus als Prüffrage in Schreibregeln und Review-Checkliste („unterstützt dieser Absatz eine Handlung oder Entscheidung?"), definierter Erstellungs- und Reviewprozess (Anleitung Kap. 10 bis 12), Warnungen vor irreversiblen Schritten **vor** dem Schritt.

**Abweichungen, begründet:**

* **Keine formale Konformitätserklärung und kein Warnhinweis-System nach Signalwortstufen** (GEFAHR/WARNUNG/VORSICHT). Unser Inhalt hat keine Personenschutz-Relevanz; ein fetter Hinweis vor irreversiblen Schritten genügt und hält die Seiten lesbar.
* **Keine formal nachgewiesene Erstellerqualifikation.** Ersatz: Peer-Review-Pflicht plus Skill handbuch-autor, der die Regeln maschinell durchsetzt. Für ein Team dieser Größe ist gelebte Prüfung wirksamer als Qualifikationsnachweise.

### DIN EN ISO 20607, ISO 12100, ANSI Z535.6 (Maschinensicherheit)

**Nicht anwendbar.** Wir dokumentieren keine Maschinen und erstellen keine Betriebsanleitungen im Sinne der Maschinenverordnung. Keine Übernahme; bewusst keine Warnhinweis-Taxonomie nach Z535.6 (siehe oben).

### ISO/IEC/IEEE 26511 bis 26515 (Software-Nutzerdokumentation)

**Fordert u.a.:** Management-, Beschaffungs-, Test-, Gestaltungs- und Agile-Prozesse für Nutzerdokumentation.

**Übernommen:** 26514 (Gestaltung) ist in der Anleitung als Referenz verankert (Struktur- und Formatanforderungen); 26515 (agil) prägt unseren schlanken Erstellungsprozess: dokumentieren im selben Arbeitsgang wie die Änderung (P9), kleine Einheiten, Review statt Big-Bang-Abnahme.

**Abweichungen, begründet:** **Keine getrennten Management- und Beschaffungsprozesse** (26511/26512): Bei einem Team ohne Doku-Abteilung und ohne Zulieferer wäre das Prozess-Theater. Die Testperspektive (26513) deckt unsere Review-Checkliste plus der Praxistest „neues Mitglied folgt der Anleitung" ab.

### VDI 4500 (Technische Dokumentation, Richtlinienreihe)

**Fordert u.a.:** systematische Gliederung, Terminologiemanagement, Lebenszyklus der Dokumentation.

**Übernommen:** Terminologie-Disziplin (S5, Seiten-Glossar als verbindliche Termliste), Lebenszyklus-Gedanke über Prüfintervalle, Freshness-Dashboard und Eskalationsregel.

**Abweichungen, begründet:** **Kein zentrales Terminologie-Register.** Wir führen Seiten-Glossare mit wortgleich wiederverwendeten Definitionen; das ist eine bewusste Ausnahme von P5 zugunsten in sich verständlicher Seiten. Ein zentrales Register lohnt erst ab deutlich größerem Begriffsbestand; die Wortgleichheits-Regel hält die Tür dafür offen.

### tekom-Leitlinie „Regelbasiertes Schreiben"

**Übernommen:** Kern unserer Schreibregeln S1 bis S8 (Aktiv, kurze Sätze, Imperativ, Konkretheit, Ein-Begriff-Regel, konsistente Anrede, keine Füllwörter) plus Standardsatzmuster für Handlungsschritte.

**Abweichungen, begründet:** Wir übernehmen die **vereinfachte Auswahl**, nicht das volle Regelwerk (über 100 Regeln): Der Nutzen zusätzlicher Regeln fällt bei internen How-tos steil ab, die Einstiegshürde für schreibende Teammitglieder stiege dagegen deutlich.

### DITA (OASIS)

**Fordert u.a.:** modulare Topic-Typen (concept/task/reference), Wiederverwendung über Referenzierung, strikte Trennung Inhalt/Ausgabe.

**Übernommen:** Die Topic-Typen-Idee, umgesetzt über Diátaxis-Seitentypen; Wiederverwendung über Verlinkung (P5); Pflicht-Kurzbeschreibung entspricht DITAs `shortdesc`.

**Abweichungen, begründet:** **Keine DITA-Toolchain (XML, Spezialeditoren).** Autorenschaft im WordPress-Block-Editor ist Kernanforderung des Konzepts (niedrige Schwelle für alle Teammitglieder); eine XML-Pipeline würde genau die Menschen ausschließen, die schreiben sollen.

### ASD-S1000D

**Nicht anwendbar.** Luftfahrt-/Verteidigungsstandard mit Datenmodul-Verwaltung; für ein Teamhandbuch massiv überdimensioniert. Keine Übernahme.

### ASD-STE100 (Simplified Technical English)

**Fordert u.a.:** kontrolliertes Vokabular, harte Satzlängenlimits, ein Wort = eine Bedeutung.

**Übernommen:** die Prinzipien, auf Deutsch übertragen: S5 (eine Bedeutung, ein Begriff), S2 mit harter 25-Wörter-Prüfung, Standardsatzmuster für Schritte.

**Abweichungen, begründet:** **Kein kontrolliertes Wörterbuch.** STE100 ist für Englisch definiert und lebt vom gepflegten Dictionary; für Deutsch existiert kein Äquivalent, und der Pflegeaufwand stünde in keinem Verhältnis. Die Glossar-Disziplin pro Seite ist unser verhältnismäßiger Ersatz.

## Organisationsdokumentation

### ISO 9001:2015 / ISO 10013:2021 (dokumentierte Information)

**Fordert u.a.:** Dokumentenhierarchie (Politik → Prozesse → Arbeitsanweisungen → Nachweise), Lenkung dokumentierter Information (Erstellung, Prüfung, Freigabe, Änderung, Versionierung), Aktualität.

**Übernommen:** Die **Dokumentenhierarchie als Einordnungsfrage** im Skill (Konzeptseite = Grundsatz, Prozessbeschreibung = Prozess, Anleitung = Arbeitsanweisung; Nachweise wie Protokolle und erledigte Issues leben im Tool, nicht im Handbuch). Lenkung: definierter Erstellungsprozess mit Review und Freigabe (Kap. 10), Versionierung über WordPress-Revisionen, Aktualität über Prüfintervalle mit Eskalation.

**Abweichungen, begründet:** **Keine formale Dokumentenlenkung mit Freigabevermerken, Verteilerlisten und gelenkten Kopien.** Wir sind kein zertifiziertes Managementsystem; WordPress-Revisionen plus sichtbare Prüf-Metadaten leisten die Nachvollziehbarkeit mit einem Bruchteil des Aufwands. Ebenso **kein Änderungsprotokoll pro Seite** (bewusster Entscheid, Anleitung Kap. 11).

### ISO/IEC 27001, ISO 15489, ISO 30301 (Informationssicherheit, Records Management)

**Nicht übernommen als System.** Relevanter Einzelpunkt: Zugriffsschutz: Das Handbuch ist produktiv intern (Login-Pflicht), öffentlich zugängliche Demo-Inhalte sind erkennbar fiktiv. Records Management (Aufbewahrung, Kassation) betrifft Protokolle und Mitgliederdaten; das ist Sache der jeweiligen Tools und Prozesse, nicht des Handbuchs. Das Handbuch dokumentiert höchstens, **wo** solche Nachweise liegen.

### BPMN 2.0 (ISO/IEC 19510) und eCH-Standards

**Fordert u.a.:** grafische Prozessnotation mit definierter Semantik.

**Abweichung, begründet:** **Prozessbeschreibungen sind bei uns text-basiert** (Auslöser, Rollen, nummerierter Ablauf, Ergebnis). Für Prozesse mit drei bis sieben Schritten und wenigen Rollen ist Text schneller zu pflegen, barriereärmer und diff-bar; BPMN-Diagramme veralten als Bilder unbemerkt. Falls später ein komplexer Prozess mit Verzweigungen dazukommt, ist ein Diagramm als **Ergänzung** (nicht Ersatz) des Textablaufs erlaubt. Die eCH-Verwaltungsstandards richten sich an Behörden; ihre konkrete Anwendbarkeit wurde nicht weiter geprüft, weil BPMN bei uns nicht eingesetzt wird.

## Zusammenfassung der übernommenen Prüfregeln

Aus dem Abgleich sind konkret in den Skill eingeflossen:

1. **82079-Minimalismus-Prüffrage** (Schreibregeln, Review-Checkliste): Jeder Absatz unterstützt eine Handlung oder Entscheidung.
2. **ISO-10013-Ebenenfrage** (Inhaltstypen): Grundsatz/Prozess/Arbeitsanweisung/Nachweis; Nachweise gehören nicht ins Handbuch.
3. **STE-Anleihe** (Schreibregeln): harte Satzlängenprüfung, Standardsatzmuster für Schritte.
4. **tekom/VDI-Terminologie-Disziplin** (Schreibregeln): Seiten-Glossar als verbindliche Termliste.
