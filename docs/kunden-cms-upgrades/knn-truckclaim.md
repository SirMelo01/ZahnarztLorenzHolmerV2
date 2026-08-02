# KNN TruckClaim CMS-Upgrade auf aktueller YooLink-Basis

Dieses Dokument ist die konkrete Arbeitsanweisung und das Protokoll fuer das Upgrade von `KNN-TruckClaim` auf eine neue aktuelle YooLink-CMS-Basis.

## Projektwerte

- Kunde: `KNN TruckClaim`
- Altes Referenzprojekt: `KNN-TruckClaim`
- Neue technische Basis: `YooLink`
- Zielprojekt: `KNN TruckClaim 2.0`
- Vorgeschlagener Repo-Name: `knn-truckclaim-2`
- Arbeitsprinzip: altes KNN-Projekt nur lesen, neue YooLink-Kopie anpassen

## Ziel

Das alte Projekt `KNN-TruckClaim` basiert auf einer alten Version des YooLink CMS. Es soll durch ein neues Projekt ersetzt werden, das technisch auf dem aktuellen YooLink CMS basiert, im oeffentlichen Frontend wie KNN TruckClaim wirkt und funktional fuer KNN TruckClaim angepasst ist.

Am Ende soll das alte KNN-Projekt vollstaendig ersetzt werden koennen. Besucher der oeffentlichen Website sollen nach dem spaeteren Deployment moeglichst keine unerwartete Aenderung bemerken. Sichtbare Aenderungen duerfen vor allem im CMS auftreten.

## Ausgangslage

- `YooLink` ist die aktuelle CMS-Basis aus diesem Workspace.
- `KNN-TruckClaim` ist das alte, aktuell deployte Kundenprojekt.
- `KNN-TruckClaim` dient ausschliesslich als Referenz fuer UI, Inhalte, Assets, CMS-Einstellungen und kundenspezifische Anpassungen.
- Das alte KNN-Projekt darf nicht veraendert werden.
- Alle Aenderungen erfolgen in einer neuen Kopie der aktuellen YooLink-Basis.

## Grundstrategie

Nicht das alte KNN-Projekt modernisieren. Stattdessen:

1. Aktuelles YooLink CMS als technische Basis nehmen.
2. Kundenanpassungen aus `KNN-TruckClaim` gezielt uebernehmen.
3. Unbenoetigte YooLink-Funktionen entfernen oder deaktivieren.
4. Oeffentliches Frontend, CMS-Einstellungen, Kundendaten und kundenspezifische Texte auf KNN TruckClaim anpassen.
5. Neues Repository vorbereiten.
6. Neues Production-Deployment auf neuem Server planen.
7. Altes KNN-Projekt erst nach erfolgreicher Abnahme offline nehmen.

## Harte Regeln

- `KNN-TruckClaim` ist read-only.
- Secrets aus dem alten Projekt duerfen uebernommen werden, wenn sie fuer den Weiterbetrieb benoetigt werden.
- Keine interne Django-App-Struktur blind umbenennen.
- Interne Namen wie `yoolink`, `ycms` oder `config` duerfen bestehen bleiben, wenn eine Umbenennung riskant waere.
- Das sichtbare CMS-Branding bleibt YooLink CMS. Nicht aus `YooLink CMS` ein `KNN TruckClaim CMS` machen.
- Das oeffentliche Frontend, Kundendaten, Inhalte und Website-Branding auf KNN TruckClaim anpassen.
- Namen nur dort aendern, wo es sauber und risikoarm ist.
- Lieber UI, Navigation und URLs reduzieren als Models oder Migrations riskant zu loeschen.

## Namens- und Branding-Regeln

Im CMS nicht auf KNN TruckClaim umbenennen:

- CMS-Titel, wenn damit die CMS-Produktmarke gemeint ist
- Login-Branding der CMS-Shell
- Sidebar-Branding der CMS-Shell
- sichtbare CMS-Produkttexte wie `YooLink CMS`
- CMS-Footer, sofern er zur CMS-Shell gehoert

Anpassen:

- oeffentliches Website-Branding
- oeffentliche Texte
- Meta-Titel und Meta-Description
- Favicons der oeffentlichen Website, falls projektspezifisch
- Logos der oeffentlichen Website
- oeffentliche Assets
- E-Mail-Texte und Absender, falls sie im Namen des Kunden versendet werden
- README und Projektbeschreibung

Kundendaten innerhalb des CMS duerfen natuerlich KNN TruckClaim enthalten, z. B. Website-Name, Kontaktinformationen, SEO-Felder oder Inhalte, die spaeter im Frontend ausgespielt werden. Nur die CMS-Produktmarke selbst soll YooLink bleiben.

Vorsichtig behandeln:

- Python Package `yoolink`
- Django App `ycms`
- `config`
- Migrations
- Importpfade
- Datenbanktabellen
- bestehende App Labels

Wenn ein interner YooLink-Name technisch bestehen bleibt, bitte im Abschlussprotokoll dokumentieren.

## Docker und lokale Entwicklung

Wenn sauber loesbar, Docker so anpassen, dass `KNN TruckClaim 2.0` lokal parallel zum originalen YooLink-Projekt laufen kann.

Zu pruefen:

- Compose-Projektname
- Container-Namen
- Volumes
- Netzwerke
- lokale Ports
- Datenbankname
- Datenbankuser
- Umgebungsvariablen
- README / Startanleitung

Keine riskanten Docker-Umbenennungen erzwingen. Wenn etwas bewusst gleich bleibt, dokumentieren.

## Funktionen entfernen oder deaktivieren

KNN TruckClaim braucht nicht den vollen YooLink-Funktionsumfang.

Zu entfernen oder mindestens aus CMS, Sidebar, Dashboard und URLs zu deaktivieren:

- Shop
- Buttons
- Preise / Pricing
- Kunden-Demos
- YooLink-spezifische Referenzen
- YooLink-spezifische Marketing-Inhalte

Beim Entfernen beachten:

- Sidebar-Navigation anpassen
- Dashboard-Kacheln anpassen
- URL-Routen pruefen
- Views und Templates nur loeschen, wenn keine Abhaengigkeiten bestehen
- JS und CSS nur entfernen, wenn nicht mehr referenziert
- Permissions und Rollen pruefen
- Tests oder Smoke Checks anpassen
- Migrations und Models nicht beschaedigen

Wenn Loeschen riskant ist, zuerst nur deaktivieren und dokumentieren.

## Oeffentliches Frontend

Die oeffentlichen YooLink-Seiten sollen durch die passenden Seiten aus dem alten `KNN-TruckClaim` ersetzt werden.

Zu pruefen und zu uebernehmen:

- Templates
- Layout
- Texte
- Bilder
- Logos
- Favicons
- statische Assets
- Kontaktinformationen
- SEO-Daten
- URLs und Slugs
- Tracking oder externe Einbindungen, falls vorhanden

Dabei pruefen:

- Welche Inhalte im alten KNN-Projekt hardcoded sind
- Welche Inhalte aus Backend- oder CMS-Daten kommen
- Welche neuen YooLink-Models oder Context Processor verwendet werden muessen
- Ob alte URLs erhalten bleiben muessen
- Ob Redirects noetig sind

Wichtig: Das Frontend soll fuer Besucher spaeter weiter wie KNN TruckClaim wirken, nicht wie YooLink.

## CMS-Seiten fuer KNN

Vor Umsetzung ein Mapping erstellen:

- Welche CMS-Bereiche gibt es im aktuellen YooLink CMS?
- Welche CMS-Bereiche hatte das alte KNN-Projekt?
- Welche Bereiche braucht KNN TruckClaim wirklich?
- Welche Bereiche muessen entfernt, deaktiviert oder ersetzt werden?
- Welche Inhalte muessen initial gesetzt werden?

Zwingende Regel:

Die alten KNN-CMS-Seiten duerfen nicht einfach unveraendert in der neuen Codebasis liegen bleiben. Wenn eine alte KNN-CMS-Seite weiterhin gebraucht wird, muss sie aktiv auf die aktuelle YooLink-CMS-Oberflaeche migriert werden:

- neues CMS-Layout verwenden
- neue Sidebar-/Dashboard-Struktur beachten
- aktuelle Form-, Modal-, Tabellen-, Button- und Karten-Patterns verwenden
- alte Template-Strukturen nicht blind kopieren
- alte CSS-/JS-Sonderloesungen nur uebernehmen, wenn sie wirklich noch noetig sind
- alte Endpunkte nur behalten, wenn sie fachlich gebraucht werden und zur neuen URL-Struktur passen
- alte CMS-Seiten, die KNN nicht mehr braucht, entfernen oder mindestens aus Navigation und URLs deaktivieren

Es reicht nicht, alte Seiten "irgendwie lauffaehig" zu machen. Jede uebernommene CMS-Seite muss aussehen und funktionieren wie ein Bestandteil der aktuellen YooLink-CMS-Oberflaeche.

Erwartung:

- Nur wichtige KNN-relevante Seiten im CMS behalten.
- YooLink-Unterseiten entfernen oder ersetzen.
- Alte KNN-CMS-Seiten nicht unveraendert liegen lassen.
- Jede benoetigte KNN-CMS-Seite auf die neue YooLink-CMS-UI migrieren.
- Dashboard und Sidebar deutlich vereinfachen.
- CMS weiterhin technisch auf aktueller YooLink-Basis halten.

## Daten und Konfiguration

Nicht nur `.env` vergleichen. Auch pruefen:

- Settings Defaults
- WebsiteSettings / UserSettings
- Logos
- Favicons
- Medien
- Uploads
- initiale CMS-Daten
- Fixtures oder Seed-Daten
- SEO-Daten
- Kontakt- und Unternehmensdaten
- Deployment-Konfiguration

Secrets:

- Alte Secrets duerfen uebernommen werden, wenn sie fuer den Weiterbetrieb erforderlich sind.
- Alte `.env` strukturell und inhaltlich pruefen.
- Benoetigte Variablen dokumentieren.
- Uebernommene Secrets nicht in Git committen.
- Neue Secrets nur dort erzeugen, wo alte Werte nicht mehr passen oder bewusst rotiert werden sollen.

## Vorgehensprotokoll

### 1. Analyse

- [ ] Neues YooLink CMS analysiert
- [ ] Altes `KNN-TruckClaim` read-only analysiert
- [ ] Oeffentliche KNN-Seiten identifiziert
- [ ] KNN-Assets identifiziert
- [ ] Alte CMS-Bereiche identifiziert
- [ ] Aktuelle YooLink-CMS-Bereiche identifiziert
- [ ] Alte KNN-CMS-Seiten identifiziert und bewertet
- [ ] Feature-Mapping erstellt
- [ ] Risiken dokumentiert

### 2. Planung

- [ ] Zu behaltende Funktionen festgelegt
- [ ] Zu entfernende Funktionen festgelegt
- [ ] Umbenennungsstrategie festgelegt
- [ ] Docker-/Port-Strategie festgelegt
- [ ] Daten- und Medienmigration geplant
- [ ] Deployment- und Rollback-Plan skizziert

### 3. Umsetzung

- [ ] Neue YooLink-Kopie fuer KNN vorbereitet
- [ ] sichtbares CMS-Branding weiterhin als YooLink CMS erhalten
- [ ] oeffentliches Branding auf KNN TruckClaim angepasst
- [ ] Docker-Komponenten bei Bedarf angepasst
- [ ] Sidebar bereinigt
- [ ] Dashboard bereinigt
- [ ] nicht benoetigte URLs deaktiviert
- [ ] nicht benoetigte CMS-Bereiche entfernt oder versteckt
- [ ] benoetigte alte KNN-CMS-Seiten auf neue YooLink-CMS-UI migriert
- [ ] alte KNN-CMS-Seiten nicht unveraendert im neuen CMS belassen
- [ ] oeffentliche KNN-Seiten uebernommen
- [ ] KNN-Assets uebernommen
- [ ] CMS-Einstellungen initial angepasst
- [ ] README / Betriebsdokumentation angepasst

### 4. Pruefung

- [ ] Django startet lokal
- [ ] CMS Login funktioniert
- [ ] Sidebar stimmt
- [ ] Dashboard stimmt
- [ ] alle sichtbaren CMS-Seiten nutzen die neue YooLink-CMS-Oberflaeche
- [ ] keine alten KNN-CMS-Seiten sind unveraendert erreichbar
- [ ] oeffentliche Startseite rendert
- [ ] wichtige oeffentliche Unterseiten rendern
- [ ] Medien / Assets laden
- [ ] keine offensichtlichen kaputten Imports
- [ ] relevante Tests oder Smoke Checks laufen
- [ ] Browser-Check im CMS durchgefuehrt
- [ ] Browser-Check im oeffentlichen Frontend durchgefuehrt

### 5. Abschluss

- [ ] Neues GitHub-Repository vorbereitet
- [ ] offene technische Altlasten dokumentiert
- [ ] bewusst erhaltene interne YooLink-Namen dokumentiert
- [ ] Production-Variablen dokumentiert
- [ ] Datenmigration dokumentiert
- [ ] Medienmigration dokumentiert
- [ ] Deployment-Plan dokumentiert
- [ ] Rollback-Plan dokumentiert
- [ ] finale Abnahme offen / erledigt

## Akzeptanzkriterien

Das Upgrade gilt als bereit fuer Staging oder Production-Vorbereitung, wenn:

- Das Projekt lokal startet.
- CMS Login funktioniert.
- Sichtbares CMS-Branding weiterhin YooLink CMS zeigt.
- YooLink-spezifische, fuer KNN irrelevante Funktionen nicht mehr sichtbar sind.
- Keine alten KNN-CMS-Seiten unveraendert im neuen CMS erreichbar sind.
- Jede benoetigte KNN-CMS-Seite an die aktuelle YooLink-CMS-Oberflaeche angepasst wurde.
- Das oeffentliche Frontend KNN TruckClaim entspricht.
- Wichtige URLs und SEO-relevante Seiten erhalten oder sauber redirected sind.
- Secrets bewusst uebernommen oder bewusst neu erzeugt wurden und nicht in Git liegen.
- Daten, Medien und Konfiguration fuer Deployment dokumentiert sind.
- Offene Risiken klar dokumentiert sind.

## Offene Punkte vor Start

- [ ] Exakter neuer Repository-Name bestaetigen
- [ ] Gewuenschte lokale Ports festlegen
- [ ] Welche KNN-CMS-Bereiche wirklich gebraucht werden, final bestaetigen
- [ ] Datenbank- und Medienmigration aus altem Production-System klaeren
- [ ] Neuer Server / Hosting-Ziel klaeren
- [ ] Domain- und DNS-Wechsel planen

## Wichtigster Grundsatz

`KNN TruckClaim 2.0` soll technisch so nah wie moeglich am aktuellen YooLink CMS bleiben, aber aeusserlich und funktional wie KNN TruckClaim wirken.

Nicht unnoetig tief in interne Strukturen eingreifen. Saubere, nachvollziehbare Anpassungen sind wichtiger als eine vollstaendige interne Umbenennung.
