# Generated by Django 3.2.7 on 2021-09-08 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0006_team_youtube_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='insra_link',
            new_name='insta_link',
        ),
    ]
