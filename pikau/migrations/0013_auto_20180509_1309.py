# Generated by Django 2.0.4 on 2018-05-09 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pikau', '0012_auto_20180509_0730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pikaucourse',
            name='cover_photo',
            field=models.CharField(default='images/pikau-course-cover.png', max_length=100),
        ),
    ]
