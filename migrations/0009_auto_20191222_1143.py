# Generated by Django 3.0 on 2019-12-22 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0008_auto_20191219_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_emoployess',
            name='acc_no',
            field=models.IntegerField(max_length=20),
        ),
    ]
