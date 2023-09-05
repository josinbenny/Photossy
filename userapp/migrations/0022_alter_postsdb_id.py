# Generated by Django 4.1.7 on 2023-05-30 05:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0021_alter_postsdb_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postsdb',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
