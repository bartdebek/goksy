# Generated by Django 4.2.6 on 2023-10-22 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='fastest_lap',
            field=models.DecimalField(decimal_places=3, max_digits=7),
        ),
    ]
