from django.db import migrations


# Diese beiden Abschnitte standen bisher fest im Template `pages/impressum.html`
# und wurden nur angezeigt, solange es ueberhaupt keine CMS-Bloecke gab. Da die
# oeffentliche Seite jetzt (wie bei YooLink) immer die Pflichtangaben aus den
# Unternehmensdaten plus die CMS-Bloecke rendert, wandern sie hier in den
# Builder, damit kein Inhalt verloren geht und sie pflegbar werden.
EXTRA_BLOCKS = [
    {
        "title": "Berufsbezeichnung",
        "content": "Zahnarzt",
        "order": 3,
    },
    {
        "title": "Markenschutz",
        "content": "Verwendete Kennzeichen sind Marken ihrer jeweiligen Eigentümer.",
        "order": 4,
    },
]


def seed(apps, schema_editor):
    ImpressumBlock = apps.get_model("cms_content", "ImpressumBlock")
    for block in EXTRA_BLOCKS:
        if ImpressumBlock.objects.filter(title=block["title"]).exists():
            continue
        ImpressumBlock.objects.create(
            active=True,
            title_de=block["title"],
            content_de=block["content"],
            **block,
        )


def unseed(apps, schema_editor):
    ImpressumBlock = apps.get_model("cms_content", "ImpressumBlock")
    ImpressumBlock.objects.filter(title__in=[b["title"] for b in EXTRA_BLOCKS]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("cms_content", "0010_remove_customer_description_en_and_more"),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
