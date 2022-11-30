# Generated by Django 4.1.3 on 2022-11-30 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('itemid', models.AutoField(primary_key=True, serialize=False)),
                ('categlory', models.CharField(default='Item', max_length=128)),
                ('itemname', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=1024)),
                ('address', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
