# Generated by Django 4.1.7 on 2023-05-17 05:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0013_postsdb_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postsdb',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
