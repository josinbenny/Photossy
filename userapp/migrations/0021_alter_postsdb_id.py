# Generated by Django 4.1.7 on 2023-05-30 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0020_alter_postsdb_no_of_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postsdb',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
