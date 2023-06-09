# Generated by Django 4.1.7 on 2023-05-30 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_user_about_user_user_avatar_user_phone_active_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='فعال'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_active_code',
            field=models.DateTimeField(blank=True, null=True, verbose_name=' فعال سازی شماره همراه'),
        ),
    ]
