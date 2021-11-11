# Generated by Django 3.2.9 on 2021-11-11 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubeapp', '0003_reply_video_pk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='video_pk',
        ),
        migrations.RemoveField(
            model_name='reply',
            name='video_pk',
        ),
        migrations.AddField(
            model_name='comment',
            name='video_id',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reply',
            name='video_id',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]