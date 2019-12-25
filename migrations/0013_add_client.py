# Generated by Django 3.0 on 2019-12-24 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0012_auto_20191223_2211'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('client_id', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('profile_pic', models.FileField(default='avatar.png', upload_to='hrms/img/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
