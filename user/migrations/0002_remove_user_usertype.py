# Generated by Django 4.1.3 on 2022-12-04 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='usertype',
        ),
    ]