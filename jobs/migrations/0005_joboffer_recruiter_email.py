# Generated by Django 5.0.1 on 2024-01-20 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_alter_joboffer_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='joboffer',
            name='recruiter_email',
            field=models.EmailField(default='Não informado', editable=False, max_length=254),
        ),
    ]
