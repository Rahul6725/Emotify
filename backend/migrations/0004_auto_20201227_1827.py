# Generated by Django 3.1.2 on 2020-12-27 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_remove_captured_images_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('song_id', models.IntegerField(default=-1)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_name', models.CharField(max_length=50)),
                ('genre_img', models.ImageField(upload_to='genre_images/')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=30)),
                ('user_img', models.ImageField(upload_to='user_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=100)),
                ('duration', models.TimeField()),
                ('artist_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.artists')),
                ('genre_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.genre')),
            ],
        ),
        migrations.CreateModel(
            name='Playlists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playlists_name', models.CharField(max_length=100)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.user')),
            ],
        ),
        migrations.AddField(
            model_name='artists',
            name='genre_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.genre'),
        ),
        migrations.AddField(
            model_name='artists',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.user'),
        ),
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=50)),
                ('album_img', models.ImageField(upload_to='album_images/')),
                ('description', models.TextField()),
                ('artist_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.artists')),
                ('genre_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.genre')),
                ('song_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.songs')),
            ],
        ),
    ]
