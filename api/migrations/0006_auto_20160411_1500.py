# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-11 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20160405_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='owned_issues_count',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='owned_repos_count',
        ),
        migrations.AddField(
            model_name='customuser',
            name='total_issues_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customuser',
            name='unassigned_issues_count',
            field=models.IntegerField(default=0),
        ),
    ]
