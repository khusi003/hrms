# Generated by Django 3.0 on 2019-12-18 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0002_add_emoployess'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_emoployess',
            name='joining_date',
            field=models.CharField(max_length=50),
        ),
    ]
