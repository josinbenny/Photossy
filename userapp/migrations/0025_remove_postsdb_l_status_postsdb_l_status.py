# Generated by Django 4.1.7 on 2023-06-05 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0024_postsdb_l_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postsdb',
            name='l_status',
        ),
        migrations.AddField(
            model_name='postsdb',
            name='l_status',
            field=models.ManyToManyField(blank=True, related_name='liked_posts', to='userapp.userdb'),
        ),
    ]
