# Zahnarzt Lorenz Holmer CMS-Upgrade auf aktueller YooLink-Basis

Dieses Dokument ist die konkrete Arbeitsanweisung und das Protokoll fuer das Upgrade von `ZahnarztLorenzHolmer` auf eine neue aktuelle YooLink-CMS-Basis.

Der Fokus der ersten Umsetzungsphase liegt bewusst eng auf Projektanpassung, Docker-Namen, oeffentlichem Frontend und dem CMS-Bereich `Seiten`. Die Grundfunktionen des aktuellen YooLink CMS sollen nicht unnoetig umgebaut werden.

## Projektwerte

- Kunde: `Zahnarzt Lorenz Holmer`
- Altes Referenzprojekt: `ZahnarztLorenzHolmer`
- Neue technische Basis: `YooLink`
- Zielprojekt: `Zahnarzt Lorenz Holmer 2.0`
- Vorgeschlagener Repo-Name: `zahnarzt-lorenz-holmer`
- Vorgeschlagener technischer Prefix: `holmer` oder `zahnarzt_lorenz_holmer`
- Arbeitsprinzip: altes Holmer-Projekt nur lesen, neue YooLink-Kopie anpassen

## Ziel

Das alte Projekt `ZahnarztLorenzHolmer` basiert auf einer sehr alten YooLink-CMS-Version. Es soll nicht technisch hochmigriert werden. Stattdessen soll das aktuelle Projekt `YooLink` als frische Basis kopiert und daraus ein neues, sauberes Kundenprojekt fuer Zahnarzt Lorenz Holmer erstellt werden.

Am Ende soll das neue Projekt technisch auf dem aktuellen YooLink CMS stehen, lokal parallel zu anderen YooLink-Kundenprojekten laufen koennen (nicht auf einem Server oder Portänderungen nur icht gleicher docker container Namen, da ich sonst nur ein Docker Container gebaut haben kann) und im oeffentlichen Frontend wie die bestehende Holmer-Website wirken.

Die erste Zielmarke ist erreicht, wenn:

- die aktuelle YooLink-Basis als Holmer-Projekt vorbereitet ist,
- Projekt- und Docker-Namen sauber vom originalen YooLink-Projekt getrennt sind,
- das oeffentliche YooLink-Frontend durch das Holmer-Frontend ersetzt wurde,
- die Holmer-Frontend-Inhalte im CMS unter `Seiten` bearbeitbar sind,
- alte YooLink-Seiten im CMS-Bereich `Seiten` entfernt, deaktiviert oder durch Holmer-Seiten ersetzt sind,
- die restlichen CMS-Grundfunktionen zunaechst moeglichst unveraendert bleiben.

## Umsetzungsstand 2026-08-01

Begonnen und umgesetzt:

- Aktuelle YooLink-Basis als neues Projekt `zahnarzt-lorenz-holmer` kopiert.
- Oeffentliche Holmer-Templates und relevante Holmer-Assets aus dem alten Referenzprojekt uebernommen.
- Lokale und Production-Docker-Namen auf Prefix `holmer` umgestellt.
- Lokale Postgres-Daten auf DB/User/Passwort `holmer` umgestellt.
- Public URL-Set auf `/`, `/kontakt/`, `/impressum/`, `/datenschutz/`, `/cookies/` und `sitemap.xml` reduziert.
- CMS-Bereich `Seiten` auf Holmer-Kacheln reduziert.
- Zielmapping fuer die Startseite als genau eine Kachel `Hauptseite` umgesetzt.
- `Hauptseite` verdrahtet Hero, Leistungen, Praxisgalerie, Team, Kontakt, FAQ und Footer mit `TextContent`, `fileentry`, `Galerie`, `TeamMember`, `FAQ` und `OpeningHours`.
- Kontakt, Impressum, Datenschutz und Cookies nutzen wieder die aktuellen CMS-Datenquellen, wo vorhanden.
- Projekt-/Domain-Defaults auf `zahnarzt-dr-holmer.de` gesetzt.
- CMS-Sidebar und Dashboard fuer Holmer reduziert: Shop, Produkte, Bestellungen, Buttons, Preise und Kunden-Demos sind nicht mehr sichtbar.
- Shop-CMS-Routen sind auskommentiert und koennen spaeter gezielt wieder aktiviert werden.
- Kunden-Demos sind aus CMS-URLs, Views, Templates und Demo-Assets entfernt.
- Developer Settings sind nur noch fuer den eingeloggten User `yoolink` sichtbar und direkt aufrufbar.
- Production-Domain-Audit durchgefuehrt: Traefik, Nginx, `ALLOWED_HOSTS`, `CSRF_TRUSTED_ORIGINS`, Canonicals, OpenAPI-Server und Django-Site-Migration zeigen auf `zahnarzt-dr-holmer.de`.
- Storage-/Upload-Defaults fuer neue Uploads auf Holmer umgestellt (`holmer/...` im gemeinsamen Bucket `yoolink`, Recovery-Prefix `private/holmer/recovery-backups`).
- SEO-/Schema.org-Fallbackdaten, neue WebsiteSettings/UserSettings-Defaults und sichtbare CMS-Placeholders auf Holmer bzw. neutrale Werte umgestellt.
- Analyse-Tracking ist fuer Holmer entfernt; die Cookie-Auswahl enthaelt nur noch notwendige Cookies und externe Dienste.
- Restbefund: `yoolink.de` kommt nur noch in alten, nicht gerouteten YooLink-Marketingtemplates vor. Diese sind weder im oeffentlichen URL-Set noch in der Holmer-`Seiten`-Uebersicht verdrahtet und wurden deshalb nicht nebenbei geloescht.

Verifikation:

- Python-Syntaxcheck mit `C:\Python311\python.exe -m compileall config yoolink` erfolgreich.
- `docker compose -f local.yml config --quiet` erfolgreich.
- `docker compose -f local.yml run --rm django python manage.py makemigrations --check --dry-run` erfolgreich.
- `docker compose -f local.yml run --rm django python manage.py check` erfolgreich.
- Template-Load-Smoke-Test fuer geaenderte Base-/CMS-/Settings-/Blog-Templates erfolgreich.
- `python manage.py check --settings=config.settings.local` lokal nicht ausfuehrbar, weil Django in der lokalen Python-Installation nicht installiert ist.
- `docker compose -f production.yml config --quiet` scheitert erwartbar, solange `.envs/.production/.django` und `.envs/.production/.postgres` fehlen.
- `python manage.py check --deploy --settings=config.settings.production` im lokalen Docker-Image scheitert erwartbar an fehlender Production-Abhaengigkeit `anymail`; fuer diesen Check muss das Production-Image bzw. die Production-Dependency-Umgebung verwendet werden.

## Ausgangslage

- `YooLink` ist die aktuelle CMS-Basis in diesem Workspace.
- `ZahnarztLorenzHolmer` ist das alte Kundenprojekt und dient nur als Referenz.
- Das alte Holmer-Projekt darf nicht veraendert werden.
- Alle Aenderungen erfolgen in einer neuen Kopie der aktuellen YooLink-Basis.
- Das sichtbare CMS-Produktbranding bleibt standardmaessig `YooLink CMS`.
- Das oeffentliche Website-Branding wird auf Zahnarzt Lorenz Holmer angepasst.

## Grundstrategie

Nicht das alte Holmer-Projekt modernisieren. Stattdessen:

1. Aktuelles `YooLink` als technische Basis kopieren.
2. Neues Projekt technisch eindeutig fuer Holmer benennen.
3. Docker-Images, Container, Volumes, Netzwerke und lokale Ports so anpassen, dass Holmer parallel zu anderen Projekten laufen kann.
4. Oeffentliche Holmer-Templates, Assets, Texte und Seitenlogik aus `ZahnarztLorenzHolmer` uebernehmen.
5. Die neue `Seiten`-Verwaltung des aktuellen YooLink CMS auf die Holmer-Website mappen.
6. YooLink-spezifische oeffentliche Seiten aus dem CMS-Bereich `Seiten` entfernen oder deaktivieren.
7. Alle anderen CMS-Features initial mitnehmen und erst danach bewusst bewerten.

## Harte Regeln

- `ZahnarztLorenzHolmer` ist read-only.
- Keine interne Django-App-Struktur blind umbenennen.
- Interne Namen wie `yoolink`, `ycms`, `config`, App Labels, Migrations und Importpfade duerfen bestehen bleiben, wenn eine Umbenennung riskant waere.
- Das sichtbare CMS-Branding bleibt `YooLink CMS`, sofern nicht spaeter explizit anders gewuenscht.
- Das oeffentliche Frontend, Kundendaten, Inhalte, SEO, Logo, Favicon und Website-Assets werden auf Zahnarzt Lorenz Holmer angepasst.
- In Phase 1 keine Grundfunktionen des aktuellen CMS tief umbauen.
- Features initial mitnehmen. Entfernen oder Deaktivieren erst nach Mapping und Smoke Checks.
- Im Bereich `Seiten` keine alten YooLink-Marketingseiten stehen lassen, wenn sie im Holmer-Projekt keinen fachlichen Zweck haben.

## Namens- und Branding-Regeln

Im CMS nicht automatisch auf Zahnarzt Lorenz Holmer umbenennen:

- CMS-Titel, wenn damit die CMS-Produktmarke gemeint ist
- Login-Branding der CMS-Shell
- Sidebar-Branding der CMS-Shell
- sichtbare CMS-Produkttexte wie `YooLink CMS`
- CMS-Footer, sofern er zur CMS-Shell gehoert

Anpassen:

- oeffentliches Website-Branding
- oeffentliche Navigation und Footer
- Meta-Titel und Meta-Description
- Logo und Favicon
- oeffentliche Bilder und Assets
- Kontaktformulare und E-Mail-Texte, falls sie im Namen der Praxis versendet werden
- README und Projektbeschreibung
- lokale Docker-/Compose-Bezeichnungen

Vorsichtig behandeln:

- Python Package `yoolink`
- Django App `ycms`
- `config`
- Migrations
- Datenbanktabellen
- bestehende URL-Namen, sofern Templates oder Tests darauf verweisen

Wenn ein interner YooLink-Name technisch bestehen bleibt, bitte im Abschlussprotokoll dokumentieren.

## Docker und lokale Entwicklung

Das neue Holmer-Projekt muss lokal parallel zum originalen `YooLink` und zu anderen Kundenprojekten laufen koennen (bzw. gebaut werden können). Deshalb sollen die Docker-Bezeichnungen im neuen Projekt einen eigenen Prefix bekommen.

Zu pruefen und anzupassen:

- Compose-Projektname, z. B. `holmer`
- Container-Namen, z. B. `holmer_local_django`, `holmer_local_postgres`, `holmer_local_redis`
- Images, z. B. `holmer_local_django`, `holmer_production_django`
- Volumes, z. B. `holmer_local_postgres_data`, `holmer_local_postgres_data_backups`
- Netzwerke, falls explizit benannt
- lokale Ports, damit kein Konflikt mit `YooLink` entsteht
- Datenbankname und Datenbankuser, z. B. `holmer`
- Umgebungsvariablen und README-Startanleitung

Nicht noetig und eher riskant:

- Python-Importpfade nur wegen Docker umzubenennen
- Django-App-Labels umzubenennen
- Migrations anzufassen, nur damit Tabellen anders heissen
- Ports ändern

## Oeffentliches Frontend

Die oeffentlichen YooLink-Seiten der aktuellen Basis sollen durch die passenden Holmer-Seiten aus `ZahnarztLorenzHolmer` ersetzt werden.

Im alten Holmer-Projekt aktuell relevante oeffentliche Seiten:

- `/` ueber `pages/index.html`
- `/kontakt/` ueber `pages/kontakt.html`
- `/impressum/` ueber `pages/impressum.html`
- `/datenschutz/` ueber `pages/datenschutz.html`
- `/cookies/` ueber `pages/cookies.html`
- `sitemap.xml`

Als Referenz vorhanden, aber fachlich zuerst pruefen:

- `pages/shop.html`
- `pages/detail.html`
- Shop-/Order-Templates im CMS
- Produktmodelle und Order-Flows

Wichtige Holmer-Assets aus dem alten Projekt:

- Logos und Favicon aus `yoolink/static/images/Logo/`
- Titelbilder aus `yoolink/static/images/Titelbild/`
- Portraits aus `yoolink/static/images/Portrait/`
- Praxis- und Shooting-Bilder aus `yoolink/static/images/Bilder Shooting/`
- Behandlungszimmer-Bilder aus `yoolink/static/images/Behandlungszimmer/`
- Behandlungs-Icons aus `yoolink/static/images/Icons Behandlungen/`
- ggf. Behandlungsfaelle aus `yoolink/static/images/Behandlungsfaelle/`

Zu uebernehmende alte Frontend-Datenbindungen:

- `FAQ`
- `TeamMember`
- `TextContent`
- `fileentry`
- `Galerie`
- `OpeningHours`
- `UserSettings` bzw. in der neuen Basis bevorzugt `WebsiteSettings` / Site Owner
- `Message` fuer Kontaktformular-Einsendungen

Wichtig: Das neue Frontend soll die aktuelle YooLink-Datenstruktur nutzen, wo sie bereits besser ist. Alte Templates duerfen nicht blind kopiert werden, wenn sie dadurch neue Models, Context Processor, Uebersetzungen oder Sicherheitslogik umgehen.

## CMS-Bereich `Seiten`

Der Bereich `Seiten` ist der wichtigste Umbaupunkt der ersten Phase.

Im aktuellen YooLink CMS sind dort viele YooLink-eigene oeffentliche Seiten verdrahtet, z. B.:

- Hauptseite
- Leistungen
- CMS-Info
- Logos
- Visitenkarte
- Medien
- Webdesign
- Webdesign Deggendorf
- Kunden / Referenzen
- Blog-Uebersicht
- Kontakt
- Impressum
- Datenschutz
- Cookies

Diese Struktur passt nicht 1:1 zu Zahnarzt Lorenz Holmer. Deshalb sollen im neuen Holmer-Projekt die `Seiten`-Kacheln, URLs, Views und Templates auf die Holmer-Website reduziert und neu verdrahtet werden.

### Ziel-Mapping

| Aktuelle YooLink-Seite | Holmer-Ziel |
| --- | --- |
| Hauptseite | Eine CMS-Kachel `Hauptseite`; darin die komplette Holmer-Startseite mit Hero, Behandlungen, Team/Praxis, Galerie, Kontakt, FAQ und Footer pflegen |
| Hauptseite / Hero | keine eigene Kachel in Phase 1; Teil des kombinierten `Hauptseite`-Editors |
| Hauptseite / Preis | keine eigene Kachel in Phase 1; fuer Holmer zunaechst nicht anzeigen, sofern keine Preis-Sektion gebraucht wird |
| Hauptseite / Team | keine eigene Kachel in Phase 1; Team/Praxisinhaber als Abschnitt im kombinierten `Hauptseite`-Editor |
| Hauptseite / FAQ | keine eigene Kachel in Phase 1; FAQ als Abschnitt im kombinierten `Hauptseite`-Editor |
| Kontakt | Holmer-Kontaktseite und Kontaktbereich |
| Impressum | Holmer-Impressum, bevorzugt mit aktuellem Impressum-Builder und Stammdaten |
| Datenschutz | Holmer-Datenschutz, bevorzugt mit aktueller PrivacyPolicy-Struktur und Tokens |
| Cookies | Holmer-Cookie-Seite |
| Leistungen / CMS / Logos / Medien / Webdesign | nicht im Holmer-Frontend anzeigen; aus `Seiten` entfernen oder deaktivieren |
| Kunden / Referenzen | nur behalten, wenn fuer Holmer wirklich benoetigt |
| Blog-Uebersicht | initial mitnehmen, aber nicht oeffentlich anzeigen, solange Holmer keinen Blog nutzt |

### Holmer-spezifische Seitenstruktur

Fuer Phase 1 reicht ein kompakter `Seiten`-Bereich:

- Startseite
- Kontakt
- Impressum
- Datenschutz
- Cookies

Wichtig: Die Startseite soll im CMS genau eine Kachel `Hauptseite` sein. Es sollen in Phase 1 keine separaten `Seiten`-Kacheln oder Unterseiten fuer Hero, Behandlungen, Team, Galerie, Kontakt, FAQ oder Footer entstehen.

Innerhalb dieser einen `Hauptseite`-Kachel sollen die Holmer-Sektionen gemeinsam bearbeitbar sein:

- Hero
- Behandlungen / Leistungen
- Team oder Praxisinhaber
- Praxisgalerie
- Kontakt
- FAQ
- Footer

Die alte Holmer-CMS-Struktur hatte dafuer u. a. folgende Content-Schluessel:

- `main_hero`
- `main_service`
- `main_service_1` bis `main_service_7`
- `main_service_1_prev`, `main_service_1_after`, `main_service_1_icon` usw.
- `main_team`
- `main_contact`
- `main_faq`
- `main_praxis`
- `footer`

Diese Schluessel koennen als Migrationshilfe dienen. In der neuen Basis duerfen sie beibehalten werden, wenn dadurch das neue Holmer-Frontend klar und wartbar bleibt. Wenn die aktuelle YooLink-Struktur bessere Namen oder Komponenten vorgibt, bitte ein sauberes Mapping dokumentieren.

## Feature-Umfang

Initial sollen alle aktuellen YooLink-CMS-Grundfunktionen mitgenommen werden, damit die neue Basis stabil bleibt und keine Abhaengigkeiten frueh kaputtgehen.

Trotzdem soll nach der Frontend- und `Seiten`-Migration bewertet werden, was im Holmer-Projekt sichtbar bleiben soll.

Wahrscheinlich behalten:

- Seiten
- Bilder / Dateien
- Galerien
- FAQ
- Team
- Oeffnungszeiten
- Einstellungen / Stammdaten
- Nachrichten / Kontaktanfragen
- Benutzer, Rollen, Security, Recovery

Initial mitnehmen, aber spaeter pruefen:

- Blog
- Buttons
- Videos
- Pricing
- Shop / Produkte / Orders
- Kunden / Referenzen
- YooLink Connect / Developer API
- Demos

Wichtig: In Phase 1 lieber nicht loeschen. Wenn ein Feature fuer Holmer nicht benoetigt wird, zuerst aus Sidebar, Dashboard und oeffentlichen URLs entfernen oder verstecken. Models, Migrations und shared Services nur anfassen, wenn das nachweislich sicher ist.

## Vorgehensprotokoll

### 1. Analyse

- [ ] Neues `YooLink` CMS analysiert
- [ ] Altes `ZahnarztLorenzHolmer` read-only analysiert
- [ ] Alte oeffentliche Holmer-Seiten identifiziert
- [ ] Alte Holmer-Assets identifiziert
- [ ] Alte Holmer-CMS-Seiten identifiziert
- [ ] Aktuelle YooLink-`Seiten`-Verwaltung analysiert
- [ ] Frontend-Content-Schluessel und Datenbindungen gemappt
- [ ] Docker-Konflikte und benoetigte neue Namen notiert
- [ ] Risiken dokumentiert

### 2. Vorbereitung

- [ ] Aktuelle YooLink-Basis als neues Holmer-Projekt kopiert
- [ ] Neuer Projektordner / Repo-Name festgelegt
- [ ] README / Projektbeschreibung auf Holmer angepasst
- [ ] Docker-Compose-Namen, Container, Images und Volumes umbenannt
- [ ] Lokale Ports kollisionsfrei gesetzt
- [ ] Datenbankname und Datenbankuser fuer lokale Entwicklung angepasst
- [ ] Interne Namen, die bewusst `yoolink` bleiben, dokumentiert

### 3. Oeffentliches Frontend

- [ ] Holmer-Templates aus altem Projekt als Referenz uebernommen
- [ ] Aktuelle YooLink-Base-Templates, Static-Handling und Security-Patterns beachtet
- [ ] Holmer-Startseite umgesetzt
- [ ] Holmer-Kontaktseite umgesetzt
- [ ] Holmer-Impressum umgesetzt
- [ ] Holmer-Datenschutz umgesetzt
- [ ] Holmer-Cookie-Seite umgesetzt
- [ ] Logos, Favicon und Bilder uebernommen
- [ ] Frontend-JS und CSS bereinigt uebernommen
- [ ] Kontaktformular speichert weiter `Message`
- [ ] Oeffnungszeiten und Stammdaten werden korrekt ausgespielt
- [ ] SEO-Bloecke, Meta-Daten und Canonicals angepasst

### 4. CMS `Seiten`

- [ ] YooLink-spezifische `Seiten`-Kacheln bewertet
- [ ] Holmer-`Seiten`-Uebersicht erstellt
- [ ] Startseite im CMS als eine Kachel `Hauptseite` umgesetzt
- [ ] Kombinierter `Hauptseite`-Editor fuer die komplette Holmer-Startseite erstellt
- [ ] Hero-Sektion im kombinierten `Hauptseite`-Editor an Holmer-Frontend verdrahtet
- [ ] Behandlungen / Leistungen im kombinierten `Hauptseite`-Editor an Holmer-Frontend verdrahtet
- [ ] Team / Praxisinhaber im kombinierten `Hauptseite`-Editor an Holmer-Frontend verdrahtet
- [ ] Praxisgalerie im kombinierten `Hauptseite`-Editor an Holmer-Frontend verdrahtet
- [ ] Kontaktbereich im kombinierten `Hauptseite`-Editor an Holmer-Frontend verdrahtet
- [ ] FAQ im kombinierten `Hauptseite`-Editor an Holmer-Frontend verdrahtet
- [ ] Footer im kombinierten `Hauptseite`-Editor an Holmer-Frontend verdrahtet
- [ ] Keine separaten `Seiten`-Kacheln fuer einzelne Startseiten-Sektionen angelegt
- [ ] Kontaktseite im CMS passend bearbeitbar
- [ ] Impressum im CMS passend bearbeitbar
- [ ] Datenschutz im CMS passend bearbeitbar
- [ ] Cookies im CMS passend bearbeitbar
- [ ] YooLink-Marketingseiten aus `Seiten` entfernt oder deaktiviert
- [ ] Alte Holmer-CMS-Seiten nicht unveraendert in neuer Basis belassen

### 5. Feature-Bewertung

- [x] Sichtbare Sidebar auf Holmer-Bedarf geprueft
- [x] Dashboard auf Holmer-Bedarf geprueft
- [x] Shop / Produkte / Orders bewertet
- [ ] Blog bewertet
- [x] Pricing bewertet
- [x] Buttons bewertet
- [ ] Kunden / Referenzen bewertet
- [x] Developer API / Connect bewertet
- [x] Demos bewertet
- [x] Nicht benoetigte Features ggf. nur aus UI/URLs deaktiviert
- [x] Technische Altlasten dokumentiert

### 6. Pruefung

- [ ] Django startet lokal
- [x] Docker-Compose-Konfiguration lokal mit Holmer-Namen geprueft
- [ ] CMS Login funktioniert
- [ ] Sidebar und Dashboard laden
- [ ] `Seiten` zeigt nur sinnvolle Holmer-Seiten
- [ ] Alle sichtbaren `Seiten`-Editoren nutzen die aktuelle YooLink-CMS-Oberflaeche
- [ ] Oeffentliche Startseite rendert
- [ ] Kontakt, Impressum, Datenschutz und Cookies rendern
- [ ] Bilder, CSS und JS laden
- [ ] Kontaktformular funktioniert
- [ ] Oeffnungszeiten werden korrekt ausgespielt
- [ ] Sitemap und wichtige URLs funktionieren
- [x] Keine offensichtlichen kaputten Imports
- [x] Relevante Smoke Checks laufen
- [ ] Browser-Check im CMS durchgefuehrt
- [ ] Browser-Check im oeffentlichen Frontend durchgefuehrt

## Akzeptanzkriterien fuer Phase 1

Phase 1 gilt als erledigt, wenn:

- das neue Holmer-Projekt auf aktueller YooLink-Basis lokal startet,
- lokale Docker-Namen und Ports nicht mit dem originalen `YooLink` kollidieren,
- das oeffentliche Frontend nicht mehr wie YooLink, sondern wie Zahnarzt Lorenz Holmer wirkt,
- die relevanten oeffentlichen Holmer-Seiten erreichbar sind,
- der CMS-Bereich `Seiten` auf Holmer zugeschnitten ist,
- die Startseite ueber eine einzige CMS-Kachel `Hauptseite` bearbeitbar und mit dem Frontend verdrahtet ist,
- alte YooLink-Marketingseiten nicht mehr als Holmer-`Seiten` sichtbar sind,
- das CMS-Produktbranding weiterhin konsistent `YooLink CMS` bleibt,
- nicht benoetigte Features nicht voreilig durch riskante Model-/Migration-Eingriffe entfernt wurden,
- offene Punkte fuer Datenmigration, Deployment und spaetere Feature-Reduktion dokumentiert sind.

## Offene Punkte vor Umsetzung

- [ ] Exakten neuen Repository-Namen bestaetigen
- [ ] Finalen technischen Prefix festlegen: `holmer` oder `zahnarzt_lorenz_holmer`
- [ ] Lokale Ports festlegen
- [ ] Klaeren, ob Shop / Produkte fuer Holmer wirklich noch gebraucht werden
- [ ] Klaeren, ob Blog gebraucht wird
- [ ] Klaeren, ob Behandlungsfaelle oeffentlich gezeigt werden sollen
- [ ] Datenbank- und Medienmigration aus dem alten Production-System planen
- [ ] Neue Production-Umgebung klaeren
- [ ] Domain- und DNS-Wechsel planen
- [ ] Rollback-Plan fuer altes Holmer-Projekt erstellen

## Wichtigster Grundsatz

`Zahnarzt Lorenz Holmer 2.0` soll technisch so nah wie moeglich am aktuellen YooLink CMS bleiben, aber oeffentlich wie die Holmer-Website wirken.

Der erste Umbau gehoert dem oeffentlichen Frontend und dem CMS-Bereich `Seiten`. Alles andere wird nur so weit angefasst, wie es fuer ein sauberes, parallel lauffaehiges Kundenprojekt noetig ist.
