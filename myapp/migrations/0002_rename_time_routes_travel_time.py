# Generated by Django 5.1.4 on 2025-01-14 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='routes',
            old_name='TIME',
            new_name='TRAVEL_TIME',
        ),
    ]
