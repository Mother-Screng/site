# Generated by Django 2.1.2 on 2018-10-22 09:53

import pydis_site.apps.api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20181020_1904'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialSnake',
            fields=[
                ('name', models.CharField(max_length=140, primary_key=True, serialize=False)),
                ('info', models.TextField()),
            ],
            bases=(pydis_site.apps.api.models.ModelReprMixin, models.Model),
        ),
    ]
