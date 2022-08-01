# Generated by Django 4.0.6 on 2022-08-01 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('REGISTROS_APP', '0004_alter_validacionestable_validado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrostable',
            name='costo',
            field=models.FloatField(blank=True, max_length=110, null=True, verbose_name='Costo'),
        ),
        migrations.AlterField(
            model_name='registrostable',
            name='folio_diario',
            field=models.FloatField(blank=True, max_length=110, null=True, verbose_name='Folio Diario'),
        ),
        migrations.AlterField(
            model_name='registrostable',
            name='num_sepomex',
            field=models.CharField(blank=True, max_length=110, null=True, verbose_name='Número de SEPOMEX'),
        ),
        migrations.AlterField(
            model_name='registrostable',
            name='peso',
            field=models.FloatField(blank=True, max_length=110, null=True, verbose_name='Peso'),
        ),
        migrations.AlterField(
            model_name='validacionestable',
            name='registro',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='REGISTROS_APP.registrostable', verbose_name='Registro'),
        ),
        migrations.AlterField(
            model_name='validacionestable',
            name='validado',
            field=models.BooleanField(blank=True, null=True, verbose_name='Validado'),
        ),
    ]