# Generated by Django 4.1.4 on 2023-01-22 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relasi', '0002_remove_kontenmodel_jenis_kontenmodel_jenis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kontenmodel',
            name='jenis',
            field=models.ManyToManyField(default='other', to='relasi.kategorimodel'),
        ),
    ]
