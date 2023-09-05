# Generated by Django 4.1.7 on 2023-05-15 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0004_alter_postsdb_posts_alter_postsdb_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postsdb',
            name='Username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='userapp.userdb'),
        ),
        migrations.AlterField(
            model_name='userdb',
            name='Username',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]