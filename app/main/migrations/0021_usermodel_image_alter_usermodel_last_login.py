# Generated by Django 5.0.6 on 2024-09-06 19:14

import django.core.validators
import main.models.user_model
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_alter_usermodel_last_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=main.models.user_model.save_user_image, validators=[django.core.validators.FileExtensionValidator(['png', 'jpeg', 'jpg'])]),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]
