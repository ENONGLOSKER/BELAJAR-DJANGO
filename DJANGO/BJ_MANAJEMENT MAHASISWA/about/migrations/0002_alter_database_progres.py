# Generated by Django 4.1.2 on 2022-10-18 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='database',
            name='progres',
            field=models.IntegerField(),
        ),
    ]