# Generated by Django 4.1.7 on 2023-05-24 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0014_alter_postsdb_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='followersdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Follower', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userapp.userdb')),
            ],
        ),
    ]