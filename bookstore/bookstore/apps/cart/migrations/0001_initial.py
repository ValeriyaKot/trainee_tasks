# Generated by Django 3.1.7 on 2021-03-25 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('book', '0003_remove_book_isbn'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('total_price', models.IntegerField(default=0)),
                ('number_of_items', models.PositiveIntegerField(default=1)),
                ('items', models.ManyToManyField(to='book.Book')),
            ],
        ),
    ]