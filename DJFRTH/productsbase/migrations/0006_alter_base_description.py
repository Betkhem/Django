# Generated by Django 3.2 on 2021-07-01 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productsbase', '0005_base_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='base',
            name='description',
            field=models.TextField(default='Add some description', max_length='255'),
        ),
    ]
