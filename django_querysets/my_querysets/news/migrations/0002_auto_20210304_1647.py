# Generated by Django 3.1.7 on 2021-03-04 16:47

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='news',
            managers=[
                ('news', django.db.models.manager.Manager()),
            ],
        ),
    ]
