# Generated by Django 3.1.1 on 2020-09-21 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favorites', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_favorites',
            name='first_favorites',
        ),
        migrations.RemoveField(
            model_name='user_favorites',
            name='second_favorites',
        ),
        migrations.RemoveField(
            model_name='user_favorites',
            name='third_favorites',
        ),
        migrations.AddField(
            model_name='user_favorites',
            name='favorites',
            field=models.ManyToManyField(related_name='user_favorites', to='favorites.Favorites'),
        ),
        migrations.AddField(
            model_name='user_favorites',
            name='ranking',
            field=models.IntegerField(default=1),
        ),
    ]
