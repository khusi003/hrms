# Generated by Django 3.0 on 2019-12-24 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0013_add_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='file',
            field=models.FileField(upload_to='hrms/img/'),
        ),
    ]
