# Generated by Django 2.1 on 2018-08-17 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20180817_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=64, verbose_name='用户名'),
        ),
    ]
