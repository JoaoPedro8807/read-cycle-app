# Generated by Django 5.0.6 on 2024-08-03 18:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0018_alter_avaliationmodel_post_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliationmodel',
            name='title',
            field=models.CharField(max_length=50, verbose_name='titulo'),
        ),
        migrations.AlterField(
            model_name='avaliationmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_avaliations', to=settings.AUTH_USER_MODEL, verbose_name='usuario'),
        ),
    ]
