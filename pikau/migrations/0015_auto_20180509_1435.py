# Generated by Django 2.0.4 on 2018-05-09 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pikau', '0014_auto_20180509_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pikaucourse',
            name='assessment_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='pikaucourse',
            name='overview',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='pikaucourse',
            name='study_plan',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='pikaucourse',
            name='trailer_video',
            field=models.URLField(blank=True),
        ),
    ]
