# Generated by Django 3.0 on 2019-12-24 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0015_holidays'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation_name', models.CharField(max_length=50)),
                ('d_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hrms.Department')),
            ],
        ),
    ]
