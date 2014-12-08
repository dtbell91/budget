# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0002_bill'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='frequency',
            new_name='frequency_count',
        ),
        migrations.AddField(
            model_name='bill',
            name='cost',
            field=models.DecimalField(default=0, max_digits=6, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bill',
            name='date_paid',
            field=models.DateField(default=datetime.datetime.now, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='service',
            name='frequency_unit',
            field=models.DecimalField(default=1, max_digits=8, decimal_places=4, choices=[(1, b'Days'), (7, b'Weeks'), (30.4375, b'Months'), (365.25, b'Years')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='service',
            name='cost',
            field=models.DecimalField(default=0, max_digits=6, decimal_places=2),
            preserve_default=True,
        ),
    ]
