# Generated by Django 2.1 on 2018-08-17 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=64, unique=True, verbose_name='用户名'),
        ),
    ]