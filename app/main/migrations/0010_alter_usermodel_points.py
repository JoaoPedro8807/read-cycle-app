# Generated by Django 5.0.6 on 2024-08-06 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_usermodel_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='points',
            field=models.IntegerField(default=100, verbose_name='Pontos'),
        ),
    ]
