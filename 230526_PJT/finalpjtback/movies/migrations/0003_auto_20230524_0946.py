# Generated by Django 3.2.18 on 2023-05-24 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_nowmovie'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='video_key',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='NowMovie',
        ),
    ]
