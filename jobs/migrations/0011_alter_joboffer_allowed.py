# Generated by Django 5.0.1 on 2024-06-04 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0010_joboffer_allowed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joboffer',
            name='allowed',
            field=models.BooleanField(default=0),
        ),
    ]
