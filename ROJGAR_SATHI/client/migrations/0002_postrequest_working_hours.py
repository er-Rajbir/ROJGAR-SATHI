# Generated by Django 5.2.3 on 2025-07-13 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postrequest',
            name='working_hours',
            field=models.PositiveIntegerField(blank=True, help_text='Estimated total working hours for this job', null=True),
        ),
    ]
