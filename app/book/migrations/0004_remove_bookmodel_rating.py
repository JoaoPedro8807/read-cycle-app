# Generated by Django 5.0.6 on 2024-07-26 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_alter_bookmodel_g_api_id_alter_bookmodel_g_api_tag_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmodel',
            name='rating',
        ),
    ]
