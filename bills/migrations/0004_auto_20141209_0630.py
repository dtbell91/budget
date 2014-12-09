# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0003_auto_20141207_1444'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='name',
            new_name='service_name',
        ),
        migrations.RemoveField(
            model_name='service',
            name='company',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.AddField(
            model_name='service',
            name='company_name',
            field=models.CharField(default='Company Name', max_length=200),
            preserve_default=False,
        ),
    ]
