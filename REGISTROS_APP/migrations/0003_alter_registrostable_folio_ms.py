# Generated by Django 4.0.6 on 2022-08-11 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('REGISTROS_APP', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrostable',
            name='folio_ms',
            field=models.CharField(blank=True, max_length=110, null=True, verbose_name='Folio MS'),
        ),
    ]
