# Generated by Django 5.0.1 on 2024-01-26 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlStaff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='password',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='username',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]