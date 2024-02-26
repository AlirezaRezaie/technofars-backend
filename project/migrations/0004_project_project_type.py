# Generated by Django 5.0.1 on 2024-02-18 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_project_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_type',
            field=models.CharField(choices=[('website', 'وبسایت'), ('app', 'اپلیکیشن موبایل'), ('ui', 'طراحی ui/ux'), ('graphic', 'گرافیک دیزاین')], default='website', verbose_name='نوع پروژه'),
        ),
    ]