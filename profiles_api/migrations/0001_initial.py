# Generated by Django 3.2.6 on 2021-08-31 14:48

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30, null=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('image', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=20, null=True)),
                ('dob', models.DateField(max_length=8)),
                ('phone', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=2)),
                ('interest', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=25), blank=True, size=None)),
                ('attended', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, size=None)),
                ('wishlist', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, size=None)),
            ],
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=1000, unique=True)),
                ('password', models.CharField(max_length=1000)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
