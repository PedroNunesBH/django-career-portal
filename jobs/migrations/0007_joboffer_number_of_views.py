# Generated by Django 5.0.1 on 2024-01-21 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_alter_joboffer_recruiter_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='joboffer',
            name='number_of_views',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
