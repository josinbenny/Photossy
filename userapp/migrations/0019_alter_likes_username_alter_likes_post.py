# Generated by Django 4.1.7 on 2023-05-25 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0018_postsdb_no_of_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='Username',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='likes',
            name='post',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
