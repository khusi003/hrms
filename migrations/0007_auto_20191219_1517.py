# Generated by Django 3.0 on 2019-12-19 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0006_auto_20191219_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_emoployess',
            name='country',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='add_emoployess',
            name='pincode',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='add_emoployess',
            name='state',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
