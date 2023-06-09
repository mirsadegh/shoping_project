# Generated by Django 4.1.7 on 2023-06-04 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_user_is_active_alter_user_phone_active_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile', verbose_name='تصویر '),
        ),
        migrations.AlterField(
            model_name='user',
            name='fullname',
            field=models.CharField(max_length=50, verbose_name='نام و نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=12, unique=True, verbose_name='شماره همراه'),
        ),
    ]
