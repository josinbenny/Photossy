# Generated by Django 4.1.7 on 2023-05-14 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_postsdb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postsdb',
            name='Posts',
            field=models.ImageField(blank=True, null=True, upload_to='posts'),
        ),
        migrations.AlterField(
            model_name='postsdb',
            name='Username',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
