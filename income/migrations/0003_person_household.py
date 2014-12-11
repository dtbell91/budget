# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('household', '0001_initial'),
        ('income', '0002_auto_20141209_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='household',
            field=models.ForeignKey(to='household.Household'),
            preserve_default=False,
        ),
    ]
