# Generated by Django 3.1.7 on 2021-03-18 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0004_auto_20210317_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
