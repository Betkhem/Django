# Generated by Django 3.2 on 2021-05-26 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productsbase', '0006_alter_base_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='base',
            name='featured',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
