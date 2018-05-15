# Generated by Django 2.0.4 on 2018-05-04 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pikau', '0003_auto_20180504_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pikaucourse',
            name='status',
            field=models.IntegerField(choices=[(1, 'Stage 1: Conceptualising'), (2, 'Stage 2: Developing'), (3, 'Stage 3: Reviewing - Academic'), (4, 'Stage 4: Reviewing - Language'), (5, 'Stage 5: Reviewing - Technical'), (6, 'Stage 6: Completed'), (7, 'Stage 7: Completed - Published to iQualify')], default=1),
        ),
    ]
