# Generated by Django 5.0.1 on 2024-02-03 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_projectimage_project_delete_project_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(null=True, upload_to='blog_images/'),
        ),
    ]