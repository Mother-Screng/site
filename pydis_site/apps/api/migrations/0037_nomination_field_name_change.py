# Generated by Django 2.2 on 2019-06-28 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0036_alter_nominations_api'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nomination',
            old_name='unnominate_reason',
            new_name='end_reason',
        ),
        migrations.RenameField(
            model_name='nomination',
            old_name='unwatched_at',
            new_name='ended_at',
        ),
    ]