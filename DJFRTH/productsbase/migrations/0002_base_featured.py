# Generated by Django 3.2 on 2021-05-26 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productsbase', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='base',
            name='featured',
            field=models.BooleanField(default='True'),
        ),
    ]
