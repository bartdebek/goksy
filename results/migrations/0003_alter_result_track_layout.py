# Generated by Django 4.2.6 on 2023-10-22 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0002_alter_result_fastest_lap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='track_layout',
            field=models.CharField(choices=[('short', 'long')], default='short', max_length=255),
        ),
    ]
