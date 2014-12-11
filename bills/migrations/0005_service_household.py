# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('household', '0001_initial'),
        ('bills', '0004_auto_20141209_0630'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='household',
            field=models.ForeignKey(default=1, to='household.Household'),
            preserve_default=False,
        ),
    ]
