# Generated by Django 3.2.19 on 2023-06-23 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20230623_0532'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='product',
            field=models.IntegerField(default=1),
        ),
    ]