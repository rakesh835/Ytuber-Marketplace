# Generated by Django 3.2.7 on 2021-09-08 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0004_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='photo',
            field=models.ImageField(default='image', upload_to='media/team/%Y/%m/%d'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='team',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
    ]