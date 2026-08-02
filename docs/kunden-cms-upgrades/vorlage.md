# Kunden-CMS-Upgrade auf aktueller YooLink-Basis

Diese Vorlage beschreibt, wie ein altes kundenangepasstes YooLink-CMS-Projekt auf eine aktuelle YooLink-CMS-Basis gehoben werden soll.

Sie ist als Arbeitsanweisung fuer KI-gestuetzte Migrationen gedacht, wenn ein Kundenprojekt auf einem alten YooLink-Fork basiert und durch eine neue, saubere Variante ersetzt werden soll.

## Platzhalter

- `[KUNDE]`: Name des Kunden oder Projekts, z. B. `KNN TruckClaim`
- `[ALT_PROJEKT]`: altes, aktuell deploytes Kundenprojekt
- `[BASIS_PROJEKT]`: aktuelle YooLink-CMS-Basis
- `[NEU_PROJEKT]`: neues Zielprojekt, z. B. `[KUNDE] 2.0`
- `[REPO_NAME]`: Name des neuen GitHub-Repositories

## Ziel

Das Projekt `[ALT_PROJEKT]` basiert auf einer alten Version des YooLink CMS. Es soll durch eine neue, aktuelle Variante ersetzt werden, die technisch auf `[BASIS_PROJEKT]` basiert.

Das Endziel ist ein neues Projekt, z. B. `[NEU_PROJEKT]`, das technisch auf dem aktuellen YooLink CMS steht, im oeffentlichen Frontend wie `[KUNDE]` wirkt und in CMS-Einstellungen, Inhalten und Funktionsumfang an `[KUNDE]` angepasst ist.

Das alte Projekt soll danach vollstaendig ersetzbar sein.

## Ausgangslage

- `[BASIS_PROJEKT]` ist die aktuelle, neue CMS-Basis und soll als technische Grundlage verwendet werden.
- `[ALT_PROJEKT]` ist das alte, aktuell deployte Kundenprojekt und dient nur als Referenz.
- Das alte Kundenprojekt darf nicht veraendert werden. Es ist read-only zu behandeln.
- Aenderungen sollen ausschliesslich im neuen Projekt erfolgen, das aus der aktuellen YooLink-CMS-Basis entsteht.

## Grundstrategie

Bitte orientiere dich bei Architektur, Codequalitaet, CMS-Struktur, Sicherheit, Docker-Setup und Backend am aktuellen YooLink CMS.

Migriere aus dem alten Kundenprojekt nur die kundenspezifischen Anpassungen:

- oeffentliches Frontend und oeffentliche Seiten
- Branding
- Texte
- Bilder und Assets
- CMS-relevante Einstellungen
- benoetigte CMS-Seiten und Inhalte
- kundenspezifische Bezeichnungen
- ggf. vorhandene Datenstrukturen, falls sie fuer den Kunden wirklich benoetigt werden

Bitte nicht versuchen, das alte Kundenprojekt technisch zu modernisieren. Stattdessen sollen die Kundenanpassungen sauber in die neue YooLink-CMS-Basis uebernommen werden.

## Wichtige Einschraenkungen

### Namen und Branding

Das sichtbare CMS-Branding soll standardmaessig YooLink CMS bleiben. Nicht automatisch aus `YooLink CMS` ein `[KUNDE] CMS` machen.

Im CMS nicht automatisch auf den Kundennamen umbenennen:

- CMS-Titel, wenn damit die CMS-Produktmarke gemeint ist
- Sidebar-Branding der CMS-Shell
- Login-Branding der CMS-Shell
- sichtbare CMS-Produkttexte wie `YooLink CMS`
- CMS-Footer, sofern er zur CMS-Shell gehoert

Anpassen:

- oeffentliches Website-Branding
- oeffentliche Texte
- Meta-Titel und Meta-Description
- Favicon, Logo und oeffentliche Assets
- E-Mail-Absender oder E-Mail-Texte, falls sie im Namen des Kunden versendet werden
- README und Projektbeschreibung

Kundendaten innerhalb des CMS duerfen natuerlich `[KUNDE]` enthalten, z. B. Website-Name, Kontaktinformationen, SEO-Felder oder Inhalte, die spaeter im Frontend ausgespielt werden. Nur die CMS-Produktmarke selbst soll YooLink bleiben, sofern nicht explizit anders gewuenscht.

Interne App- und Ordnerstruktur nur sehr vorsichtig umbenennen.

Wichtig:

- Den obersten Projektordner darfst du in Richtung `[REPO_NAME]` oder `[KUNDE]` umbenennen, wenn sinnvoll.
- Interne Django-App-Strukturen wie `yoolink`, `ycms`, `config` usw. sollen nicht blind umbenannt werden, wenn dadurch Imports, Migrations, Settings oder Deployments kaputtgehen koennten.
- Namen nur dort aendern, wo es sauber und risikoarm loesbar ist.
- Falls ein interner Name technisch besser erhalten bleibt, bitte belassen und kurz dokumentieren.

### Docker und lokale Entwicklung

Wenn sauber moeglich, bitte Docker-Komponenten so anpassen, dass das neue Kundenprojekt lokal parallel zum originalen YooLink-Projekt laufen kann.

Bitte pruefen und ggf. anpassen:

- Compose-Projektname
- Container-Namen
- Volumes
- Netzwerke
- lokale Ports
- Datenbankname
- Datenbankuser
- Umgebungsvariablen
- README / Startanleitung

Keine Umbenennung vornehmen, wenn sie unnoetig riskant ist. Lieber sauber dokumentieren.

## Funktionsumfang reduzieren

Das neue Kundenprojekt braucht eventuell nicht alle YooLink-CMS-Funktionen. Bitte alles entfernen oder deaktivieren, was fuer `[KUNDE]` nicht gebraucht wird.

Typische Kandidaten:

- Shop
- Buttons
- Preise / Pricing
- Kunden-Demos
- YooLink-spezifische Referenzen
- YooLink-spezifische Marketing-Inhalte

Bitte dabei sauber vorgehen:

- Sidebar-Navigation anpassen
- Dashboard anpassen
- URLs und Endpunkte entfernen oder deaktivieren
- Views, Templates und JS nur loeschen, wenn keine Abhaengigkeiten mehr bestehen
- Permissions und Rollen pruefen
- Tests anpassen
- Keine Migrations oder Models beschaedigen, wenn dadurch bestehende Datenbankstruktur oder Django-Start kaputtgehen koennte

Wenn Loeschen riskant ist, bitte zunaechst aus UI, Navigation und URLs entfernen und technische Altlasten dokumentieren.

## Oeffentliches Frontend

Alle alten oeffentlichen YooLink-Seiten sollen durch die passenden oeffentlichen Seiten aus `[ALT_PROJEKT]` ersetzt werden.

Bitte dabei pruefen:

- Welche Templates im alten Kundenprojekt oeffentlich verwendet werden
- Welche statischen Assets benoetigt werden
- Welche Inhalte hardcoded sind
- Welche Inhalte aus CMS- oder Backend-Daten gezogen werden
- Ob alte Kundentemplates an neue Models, Context Processor oder CMS-Daten angepasst werden muessen
- Ob URLs, Slugs und SEO-Daten gleich bleiben muessen, damit das spaetere Deployment fuer Besucher moeglichst unveraendert wirkt

Wichtig: Fuer Besucher der oeffentlichen Website soll sich nach dem spaeteren Deployment moeglichst nichts sichtbar verschlechtern oder unerwartet aendern. Aenderungen duerfen vor allem im CMS sichtbar sein.

## CMS-Seiten und Inhalte

Bitte die normalen YooLink-CMS-Seiten und Unterseiten entfernen oder ersetzen, sodass nur die fuer `[KUNDE]` wichtigen CMS-Bereiche vorhanden sind.

Bitte vorher ein Mapping erstellen:

- Welche CMS-Bereiche hat das aktuelle YooLink CMS?
- Welche davon braucht `[KUNDE]`?
- Welche hatte das alte Kundenprojekt?
- Welche Seiten muessen uebernommen, angepasst oder entfernt werden?

Zwingende Regel:

Alte Kunden-CMS-Seiten duerfen nicht einfach unveraendert in der neuen Codebasis liegen bleiben. Wenn eine alte Kunden-CMS-Seite weiterhin gebraucht wird, muss sie aktiv auf die aktuelle YooLink-CMS-Oberflaeche migriert werden:

- neues CMS-Layout verwenden
- neue Sidebar-/Dashboard-Struktur beachten
- aktuelle Form-, Modal-, Tabellen-, Button- und Karten-Patterns verwenden
- alte Template-Strukturen nicht blind kopieren
- alte CSS-/JS-Sonderloesungen nur uebernehmen, wenn sie wirklich noch noetig sind
- alte Endpunkte nur behalten, wenn sie fachlich gebraucht werden und zur neuen URL-Struktur passen
- alte CMS-Seiten, die der Kunde nicht mehr braucht, entfernen oder mindestens aus Navigation und URLs deaktivieren

Es reicht nicht, alte Seiten "irgendwie lauffaehig" zu machen. Jede uebernommene CMS-Seite muss aussehen und funktionieren wie ein Bestandteil der aktuellen YooLink-CMS-Oberflaeche.

Erwartung:

- Nur wichtige kundenrelevante Seiten im CMS behalten.
- Alte YooLink-Unterseiten entfernen oder ersetzen, wenn sie fuer den Kunden nicht gebraucht werden.
- Alte Kunden-CMS-Seiten nicht unveraendert liegen lassen.
- Jede benoetigte Kunden-CMS-Seite auf die neue YooLink-CMS-UI migrieren.
- Dashboard und Sidebar an den reduzierten Kundenumfang anpassen.
- CMS weiterhin technisch auf aktueller YooLink-Basis halten.

## Daten und Konfiguration

Bitte auf alle relevanten Daten ausserhalb von `.env` achten:

- Settings Defaults
- WebsiteSettings / UserSettings
- Logos
- Favicons
- Medien
- initiale CMS-Daten
- Fixtures oder Seed-Daten
- statische Assets
- SEO-Daten
- Kontakt- und Unternehmensdaten
- Deployment-relevante Konfiguration

Secrets aus dem alten Projekt duerfen uebernommen werden, wenn sie fuer den Weiterbetrieb benoetigt werden. Alte `.env`-Werte strukturell und inhaltlich pruefen, benoetigte Variablen dokumentieren und Secrets nicht in Git committen. Neue Secrets nur dort erzeugen, wo alte Werte nicht mehr passen oder bewusst rotiert werden sollen.

## Vorgehensweise

Bitte nicht sofort grossflaechig loeschen oder umbenennen.

Arbeite in dieser Reihenfolge:

1. Beide Projekte analysieren.
2. Eine kurze Bestandsaufnahme erstellen:
   - aktuelles YooLink CMS
   - altes Kundenprojekt
   - Unterschiede
   - benoetigte Features
   - nicht benoetigte Features
3. Einen konkreten Migrationsplan erstellen.
4. Erst danach die neue YooLink-Kopie schrittweise in Richtung `[KUNDE]` anpassen.
5. Nach jedem groesseren Schritt pruefen:
   - Django startet
   - URLs funktionieren
   - CMS Login funktioniert
   - Sidebar und Dashboard stimmen
   - alle sichtbaren CMS-Seiten die neue YooLink-CMS-Oberflaeche nutzen
   - keine alten Kunden-CMS-Seiten unveraendert erreichbar sind
   - oeffentliche Seiten rendern
   - keine offensichtlichen kaputten Imports bestehen
   - Tests oder mindestens Smoke Checks laufen
6. Abschliessend dokumentieren:
   - was uebernommen wurde
   - was entfernt oder deaktiviert wurde
   - was bewusst intern noch `yoolink` heisst
   - welche offenen Punkte vor Production-Deployment bleiben

## Deployment-Ziel

Am Ende soll ein neues GitHub-Repository fuer `[NEU_PROJEKT]` vorbereitet werden koennen.

Das neue Projekt soll spaeter auf einem neuen Server in Production deployt werden. Danach soll das alte Kundenprojekt offline genommen werden koennen.

Bitte Production-Deployment nicht blind durchfuehren, sondern zuerst:

- lokale Tests
- Staging- oder Preview-Test
- Daten- und Medienmigration
- Backup des alten Systems
- DNS- und Domain-Plan
- Rollback-Plan
- finale Abnahme

## Wichtigster Grundsatz

Das neue Projekt soll technisch so nah wie moeglich am aktuellen YooLink CMS bleiben, aber aeusserlich und funktional wie `[KUNDE]` wirken.

Nicht unnoetig tief in die interne Struktur eingreifen. Lieber saubere, nachvollziehbare Anpassungen als riskante Komplett-Umbenennungen.

## Beispiel fuer KNN TruckClaim

- `[KUNDE]`: `KNN TruckClaim`
- `[ALT_PROJEKT]`: `KNN-TruckClaim`
- `[BASIS_PROJEKT]`: `YooLink`
- `[NEU_PROJEKT]`: `KNN TruckClaim 2.0`
- `[REPO_NAME]`: `knn-truckclaim-2`

Bei KNN TruckClaim sollen insbesondere YooLink-spezifische Funktionen wie Shop, Buttons, Preise und Kunden-Demos entfernt oder deaktiviert werden. Das oeffentliche Frontend soll sich am alten KNN-TruckClaim-Projekt orientieren, waehrend CMS, Architektur und Deployment-Basis vom aktuellen YooLink CMS kommen.
