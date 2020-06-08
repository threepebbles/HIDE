# Generated by Django 3.0.6 on 2020-05-22 10:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hide', '0008_auto_20200522_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='myfile',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='myfile',
            name='index',
            field=models.IntegerField(db_column='INDEX', unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='myfile',
            unique_together={('author', 'index')},
        ),
    ]
