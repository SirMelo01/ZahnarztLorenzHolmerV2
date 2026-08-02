# Zahnarzt Lorenz Holmer

Frisches Kundenprojekt fuer Zahnarzt Dr. Lorenz Holmer auf aktueller YooLink-CMS-Basis.

Die alte Codebasis `ZahnarztLorenzHolmer` dient nur als Referenz. Dieses Projekt ist die neue, saubere Migration mit aktuellem YooLink CMS, Holmer-Frontend und separaten Docker-Namen.

Docker Compose kann je nach Installation als `docker-compose` oder `docker compose` ausgefuehrt werden. Die Befehle unten bleiben nah am originalen YooLink-README und nutzen `docker-compose`.

## Local

### Webseite starten

```bash
docker-compose -f local.yml build
docker-compose -f local.yml up
```

### Webseite im Hintergrund starten

```bash
docker-compose -f local.yml up -d
```

### Logs ansehen

```bash
docker-compose -f local.yml logs -f
docker-compose -f local.yml logs -f django
```

### Container stoppen

```bash
docker-compose -f local.yml down
```

### Django Migrations

```bash
docker-compose -f local.yml run --rm django python manage.py makemigrations
docker-compose -f local.yml run --rm django python manage.py migrate
```

### Superuser erstellen

```bash
docker-compose -f local.yml run --rm django python manage.py createsuperuser
```

### Django Shell

```bash
docker-compose -f local.yml run --rm django python manage.py shell
```

### App erstellen

```bash
docker-compose -f local.yml run --rm django python manage.py startapp namederapp
```

### Static Files / Compress

```bash
docker-compose -f local.yml run --rm django python manage.py collectstatic
docker-compose -f local.yml run --rm django python manage.py compress --force
```

### Translations

Templates:

```django
{% load i18n %}
{% trans "FAQ_TITLE" %}
```

Befehle:

```bash
docker-compose -f local.yml run --rm django python manage.py makemessages -l de -l en
docker-compose -f local.yml run --rm django python manage.py compilemessages
```

### Tests

```bash
docker-compose -f local.yml run --rm django pytest
```

```bash
docker-compose -f local.yml run --rm django pytest --create-db
```

Nur das CMS-/Public-Sicherheitsnetz fuer Holmer:

```bash
docker-compose -f local.yml run --rm django pytest tests/test_cms_2fa.py tests/test_cms_core_modules.py tests/test_public_pages_safety_net.py
```

Shop-/Produkt-/Bestellrouten sind fuer Holmer aktuell deaktiviert. Die Shop-Tests bleiben im Projekt und sind relevant, wenn der Shop spaeter wieder aktiviert wird.

## Production

Vor dem Production-Start muessen diese Dateien vorhanden sein:

- `.envs/.production/.django`
- `.envs/.production/.postgres`

Production-Defaults zeigen auf `zahnarzt-dr-holmer.de` und `www.zahnarzt-dr-holmer.de`.
Traefik, Nginx, Canonicals, OpenAPI-Server und die Django-Site-Migration sind auf diese Holmer-Domain gesetzt.

Wichtige Production-Env-Werte in `.envs/.production/.django`:

```bash
DJANGO_ALLOWED_HOSTS=zahnarzt-dr-holmer.de,www.zahnarzt-dr-holmer.de
DJANGO_CSRF_TRUSTED_ORIGINS=https://zahnarzt-dr-holmer.de,https://www.zahnarzt-dr-holmer.de
DJANGO_DEFAULT_FROM_EMAIL="Zahnarztpraxis Dr. Lorenz Holmer <noreply@zahnarzt-dr-holmer.de>"
DJANGO_EMAIL_SUBJECT_PREFIX="[Zahnarzt Holmer]"

AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_STORAGE_BUCKET_NAME=yoolink
AWS_S3_ENDPOINT_URL=https://fra1.digitaloceanspaces.com/
AWS_LOCATION=https://yoolink.fra1.digitaloceanspaces.com/

RECOVERY_BACKUP_BUCKET_NAME=yoolink
RECOVERY_BACKUP_PREFIX=private/holmer/recovery-backups
RECOVERY_BACKUP_ENCRYPTION_KEY=
```

Der DigitalOcean Space bleibt der gemeinsame Bucket `yoolink`; neue CMS-Medien werden projektgetrennt ueber die Model-Upload-Pfade unter `holmer/...` abgelegt.

### In Projektordner wechseln

```bash
cd zahnarzt-lorenz-holmer
```

### Webseite starten

```bash
docker-compose -f production.yml build
docker-compose -f production.yml up
```

### Webseite im Hintergrund starten

```bash
docker-compose -f production.yml up -d
```

### Logs ansehen

```bash
docker-compose -f production.yml logs -f
docker-compose -f production.yml logs -f django
```

### Container stoppen

```bash
docker-compose -f production.yml down
```

### Django Migrations

```bash
docker-compose -f production.yml run --rm django python manage.py makemigrations
docker-compose -f production.yml run --rm django python manage.py migrate
```

### Superuser erstellen

```bash
docker-compose -f production.yml run --rm django python manage.py createsuperuser
```

### Django Shell

```bash
docker-compose -f production.yml run --rm django python manage.py shell
```

### Static Files / Compress

```bash
docker-compose -f production.yml run --rm django python manage.py collectstatic
docker-compose -f production.yml run --rm django python manage.py compress --force
```

### Translations Production

```bash
docker-compose -f production.yml run --rm django python manage.py makemessages -l de -l en
docker-compose -f production.yml run --rm django python manage.py compilemessages
```

### Production Check vor Deployment

Nicht gegen die echte Produktionsdatenbank testen. Vorher eine separate Test-Env oder Staging-Env nutzen.

```bash
docker-compose -f local.yml run --rm django pytest
docker-compose -f production.yml run --rm django python manage.py check --deploy --settings=config.settings.production
```

### Production Env-Dateien manuell anlegen

```bash
mkdir -p .envs/.production
nano .envs/.production/.django
nano .envs/.production/.postgres
```

Die Production-Dateien enthalten server- und kundenbezogene Secrets und werden deshalb nicht aus dem alten Projekt blind uebernommen.

## Tailwind

```bash
npm run build
npm run watch
```

Die aktuelle YooLink-CSS bleibt erhalten. Fuer das uebernommene Holmer-Frontend liegt die alte gebaute CSS zusaetzlich als `yoolink/static/css/holmer-output.css` vor.

## Docker-Namen

Lokale Docker-Namen:

- `holmer_local_django`
- `holmer_local_postgres`
- `holmer_local_redis`
- `holmer_local_celeryworker`
- `holmer_local_celerybeat`
- `holmer_local_flower`
- `holmer_local_docs`

Production Docker-Namen:

- `holmer_production_django`
- `holmer_production_postgres`
- `holmer_production_traefik`
- `holmer_production_celeryworker`
- `holmer_production_celerybeat`
- `holmer_production_flower`
- `holmer_production_nginx`

Lokale Datenbank:

- DB: `holmer`
- User: `holmer`
- Passwort: `holmer`

## CMS

Der CMS-Produktname bleibt `YooLink CMS`.

Im Bereich `Seiten` sind fuer Phase 1 nur die Holmer-relevanten Seiten sichtbar:

- Hauptseite
- Kontakt
- Impressum
- Datenschutz
- Cookies

Die Startseite wird ueber genau eine Kachel `Hauptseite` gepflegt. Darin liegen Hero, Leistungen, Praxisgalerie, Team, Kontakt, FAQ und Footer.

## Recovery Backups

Anleitung fuer lokale Downloads, automatische verschluesselte Remote-Backups, Env-Variablen und Restore:

```text
docs/yoolink-recovery-backups.md
```

## Deployment

Allgemeine YooLink-Deployment-Referenz aus dem Originalprojekt:

```text
https://www.youtube.com/watch?v=DLxcyndCvO4
```

Server-Zugang und konkrete Holmer-Production-Secrets muessen projektspezifisch gesetzt werden.

## Fehlerbehebung: Speicher voll

```bash
df -h
docker system df

docker buildx prune -af
docker builder prune -af
docker image prune -af
docker container prune -f

docker compose -f production.yml build --no-cache django
docker compose -f production.yml up
```

## Hinweise

Interne Python/Django-Namen wie `yoolink`, `ycms` und `config` bleiben bewusst bestehen, damit Migrations, App Labels und Imports stabil bleiben.
