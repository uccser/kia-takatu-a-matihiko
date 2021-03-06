# Generated by Django 2.0.6 on 2018-06-10 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0008_auto_20180610_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='author',
            field=models.CharField(blank=True, max_length=200, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='file',
            name='title',
            field=models.CharField(max_length=200, unique=True, verbose_name='Title'),
        ),
    ]
