# Generated by Django 3.0 on 2019-12-24 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0014_auto_20191224_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='Holidays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('day', models.CharField(max_length=50)),
            ],
        ),
    ]