# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 13:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product2',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': '"salesforce"."product2"',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cst_name', models.CharField(max_length=32)),
                ('cst_surname', models.CharField(max_length=32)),
                ('cst_phone', models.CharField(max_length=32)),
                ('cst_email', models.CharField(max_length=32)),
                ('cst_city', models.CharField(max_length=32)),
                ('cst_street', models.CharField(max_length=32)),
                ('cst_postal_code', models.CharField(max_length=32)),
                ('productID', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('currency', models.CharField(max_length=32)),
                ('picture', models.CharField(max_length=255)),
            ],
        ),
    ]
