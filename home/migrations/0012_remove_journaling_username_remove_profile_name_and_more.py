# Generated by Django 4.0.6 on 2022-10-30 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_remove_journaling_name_remove_profile_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journaling',
            name='username',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
        migrations.AddField(
            model_name='journaling',
            name='name',
            field=models.ForeignKey(blank=True, max_length=1000, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(default='', max_length=100),
        ),
    ]
