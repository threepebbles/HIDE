# Generated by Django 3.0.6 on 2020-05-22 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hide', '0005_auto_20200522_1731'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='myfile',
            index=models.Index(fields=['index', 'author'], name='hide_myfile_INDEX_693784_idx'),
        ),
    ]
