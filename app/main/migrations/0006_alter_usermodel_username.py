# Generated by Django 5.0.6 on 2024-07-24 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_usermodel_city_alter_usermodel_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='username',
            field=models.CharField(max_length=50, verbose_name='username'),
        ),
    ]
