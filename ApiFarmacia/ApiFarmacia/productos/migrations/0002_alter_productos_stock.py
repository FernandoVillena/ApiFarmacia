# Generated by Django 3.2.3 on 2022-06-20 08:06

import ApiFarmacia.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='stock',
            field=models.IntegerField(validators=[ApiFarmacia.utils.max_min_validator]),
        ),
    ]