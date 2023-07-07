# Generated by Django 3.2.19 on 2023-06-23 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='firstName',
            new_name='firstName1',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='lastName',
            new_name='firstName2',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='number',
            new_name='number1',
        ),
        migrations.AddField(
            model_name='user',
            name='lastName1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='lastName2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='number2',
            field=models.IntegerField(default=1),
        ),
    ]
