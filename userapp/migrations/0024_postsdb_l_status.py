# Generated by Django 4.1.7 on 2023-06-02 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0023_postsdb_post_date_alter_postsdb_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='postsdb',
            name='l_status',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
