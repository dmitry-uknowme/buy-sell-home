# Generated by Django 3.0.6 on 2020-06-13 12:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20200613_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 13, 12, 12, 21, 579975, tzinfo=utc), verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='building',
            name='img',
            field=models.ImageField(default='noimg.jpg', upload_to='img', verbose_name='Картинка'),
        ),
    ]
