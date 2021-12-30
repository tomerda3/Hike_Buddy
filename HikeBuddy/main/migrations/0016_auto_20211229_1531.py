# Generated by Django 3.2.9 on 2021-12-29 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_remove_guideinfo_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guideinfo',
            name='location',
        ),
        migrations.AddField(
            model_name='guideinfo',
            name='routes',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
