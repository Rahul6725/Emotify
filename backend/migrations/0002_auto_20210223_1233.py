# Generated by Django 2.1.1 on 2021-02-23 07:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Songs_Metadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=80)),
                ('album_img', models.ImageField(upload_to='album_images/')),
                ('artist_name', models.CharField(max_length=50)),
                ('genre_name', models.CharField(default='miscellaneous', max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='albums',
            name='artist_id',
        ),
        migrations.RemoveField(
            model_name='albums',
            name='genre_id',
        ),
        migrations.RemoveField(
            model_name='albums',
            name='song_id',
        ),
        migrations.RemoveField(
            model_name='artists',
            name='genre_id',
        ),
        migrations.RemoveField(
            model_name='artists',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='playlists',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='songs',
            name='artist_id',
        ),
        migrations.RemoveField(
            model_name='songs',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='songs',
            name='genre_id',
        ),
        migrations.RemoveField(
            model_name='songs',
            name='song_name',
        ),
        migrations.AddField(
            model_name='songs',
            name='song_file',
            field=models.FileField(default=django.utils.timezone.now, upload_to='song_files/'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Albums',
        ),
        migrations.DeleteModel(
            name='Artists',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.DeleteModel(
            name='Playlists',
        ),
        migrations.AddField(
            model_name='songs_metadata',
            name='song_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Songs', unique=True),
        ),
    ]
