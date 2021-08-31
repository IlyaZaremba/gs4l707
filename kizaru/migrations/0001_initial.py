# Generated by Django 3.2.6 on 2021-08-30 14:52

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InputModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=30)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]