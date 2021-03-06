# Generated by Django 3.0.6 on 2020-05-22 09:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hide', '0007_auto_20200522_1738'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='myfile',
            name='hide_myfile_INDEX_693784_idx',
        ),
        migrations.AlterField(
            model_name='myfile',
            name='index',
            field=models.IntegerField(db_column='INDEX', primary_key=True, serialize=False),
        ),
        migrations.AlterUniqueTogether(
            name='myfile',
            unique_together={('index', 'author')},
        ),
        migrations.RemoveField(
            model_name='myfile',
            name='id',
        ),
    ]
