# Generated by Django 5.0.1 on 2024-01-31 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_person_about_me'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='about_me',
            field=models.TextField(verbose_name='درباره من'),
        ),
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(default='admin', max_length=100, unique=True),
        ),
    ]
