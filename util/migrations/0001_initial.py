# Generated by Django 5.0.1 on 2024-02-17 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(verbose_name='موضوع پیام')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل فرستنده')),
                ('body', models.TextField(verbose_name='متن پیام')),
            ],
        ),
    ]
