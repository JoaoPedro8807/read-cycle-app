# Generated by Django 5.0.6 on 2024-07-29 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_remove_bookmodel_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmodel',
            name='author',
        ),
        migrations.RemoveField(
            model_name='bookmodel',
            name='g_api_id',
        ),
        migrations.RemoveField(
            model_name='bookmodel',
            name='g_api_tag',
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='authors',
            field=models.CharField(default='e', max_length=100, verbose_name='autor'),
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='book_api_id',
            field=models.CharField(blank=True, max_length=50, verbose_name='google api id'),
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='book_api_tag',
            field=models.CharField(blank=True, max_length=50, verbose_name='google api tag'),
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='language',
            field=models.CharField(default='e', max_length=5, verbose_name='idioma'),
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='total_pages',
            field=models.IntegerField(default=1, verbose_name='número de paginas'),
        ),
    ]
