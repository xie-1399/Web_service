# Generated by Django 2.0.6 on 2018-07-10 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host_management', '0004_auto_20180709_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostinfo',
            name='network',
            field=models.IntegerField(blank=True, null=True, verbose_name='带宽'),
        ),
        migrations.AlterField(
            model_name='hostinfo',
            name='normal_pass',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='普通用户密码'),
        ),
        migrations.AlterField(
            model_name='hostinfo',
            name='normal_user',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='普通用户'),
        ),
    ]