# Generated by Django 5.0.1 on 2024-01-07 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id_staff', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=80, null=True)),
                ('telefono', models.CharField(blank=True, max_length=10, null=True)),
                ('departamento', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
