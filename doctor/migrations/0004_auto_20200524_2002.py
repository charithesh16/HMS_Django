# Generated by Django 3.0.5 on 2020-05-24 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_auto_20200524_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
