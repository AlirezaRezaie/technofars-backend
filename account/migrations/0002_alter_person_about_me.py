# Generated by Django 5.0.1 on 2024-02-26 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='about_me',
            field=models.TextField(blank=True, null=True, verbose_name='درباره من'),
        ),
    ]
