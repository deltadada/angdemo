# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-09 15:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gemstore', '0003_reviews_stars'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gemimgs',
            old_name='gemImg_id',
            new_name='gemImgs_id',
        ),
        migrations.RemoveField(
            model_name='gems',
            name='images',
        ),
        migrations.RemoveField(
            model_name='gems',
            name='reviews',
        ),
        migrations.AddField(
            model_name='gemimgs',
            name='gem',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to='gemstore.Gems'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reviews',
            name='gem',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to='gemstore.Gems'),
            preserve_default=False,
        ),
    ]