# Generated by Django 3.0.1 on 2020-01-10 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donate', '0003_auto_20200110_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_DOB',
            field=models.DateField(),
        ),
    ]