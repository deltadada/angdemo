# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-09 15:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gemstore', '0004_auto_20160209_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='gems',
            name='name',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gemimgs',
            name='gem',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='gemstore.Gems'),
        ),
        migrations.AlterField(
            model_name='gems',
            name='description',
            field=models.CharField(blank=True, max_length=1056, null=True),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='gem',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='gemstore.Gems'),
        ),
    ]
