# Generated by Django 4.1.7 on 2023-05-28 19:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about_user',
            field=models.TextField(blank=True, null=True, verbose_name='درباره شخص'),
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile', verbose_name='تصویر اواتار'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_active_code',
            field=models.CharField(default=datetime.datetime(2023, 5, 28, 19, 10, 6, 48491), max_length=100, verbose_name='کد فعال سازی ایمیل'),
        ),
    ]