# Generated by Django 3.0 on 2019-12-19 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0004_auto_20191218_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_emoployess',
            name='otp',
            field=models.IntegerField(default=459),
        ),
    ]
