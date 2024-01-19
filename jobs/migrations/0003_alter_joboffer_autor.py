# Generated by Django 5.0.1 on 2024-01-19 13:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_joboffer_autor'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='joboffer',
            name='autor',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='car_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
