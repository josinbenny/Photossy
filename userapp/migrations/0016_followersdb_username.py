# Generated by Django 4.1.7 on 2023-05-24 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0015_followersdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='followersdb',
            name='Username',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]