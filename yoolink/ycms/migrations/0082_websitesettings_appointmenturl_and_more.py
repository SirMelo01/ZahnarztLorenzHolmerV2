from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ycms", "0081_remove_anyfile_description_en_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="websitesettings",
            name="appointmentURL",
            field=models.URLField(blank=True, default=""),
        ),
        migrations.AddField(
            model_name="websitesettings",
            name="emergencyURL",
            field=models.URLField(blank=True, default=""),
        ),
        migrations.AlterField(
            model_name="pagelink",
            name="path",
            field=models.CharField(
                help_text="Pfad der Seite, z.B. '/' oder '/impressum/'",
                max_length=300,
                verbose_name="Seitenpfad",
            ),
        ),
    ]
