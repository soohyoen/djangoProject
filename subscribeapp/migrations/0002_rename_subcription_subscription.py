# Generated by Django 3.2.6 on 2021-08-19 06:45

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projectapp', '0002_rename_projecct_project'),
        ('subscribeapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subcription',
            new_name='Subscription',
        ),
    ]
