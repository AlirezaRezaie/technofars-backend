# Generated by Django 5.0.1 on 2024-02-26 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0002_rename_creators_podcast_hosts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcast',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='podcasts/audio'),
        ),
    ]
