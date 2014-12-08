# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('expected_salary', models.DecimalField(default=0, max_digits=9, decimal_places=2)),
                ('pay_frequency_unit', models.DecimalField(default=1, max_digits=8, decimal_places=4, choices=[(1, b'Days'), (7, b'Weeks'), (30.4375, b'Months'), (365.25, b'Years')])),
                ('pay_frequency_count', models.IntegerField()),
                ('employer', models.ForeignKey(to='income.Employer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(default=datetime.datetime.now, blank=True)),
                ('amount', models.DecimalField(default=0, max_digits=9, decimal_places=2)),
                ('job', models.ForeignKey(to='income.Job')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='job',
            name='person',
            field=models.ForeignKey(to='income.Person'),
            preserve_default=True,
        ),
    ]
