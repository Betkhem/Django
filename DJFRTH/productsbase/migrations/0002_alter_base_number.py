# Generated by Django 3.2 on 2021-07-01 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productsbase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='base',
            name='number',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=50),
        ),
    ]
