# Generated by Django 2.1 on 2018-08-03 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_auto_20180802_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='api_id',
            field=models.CharField(max_length=128),
        ),
    ]