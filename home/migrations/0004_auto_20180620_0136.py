# Generated by Django 2.0 on 2018-06-19 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20180614_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketpost',
            name='photo',
            field=models.ImageField(upload_to='market/%Y/%m/%d'),
        ),
    ]
