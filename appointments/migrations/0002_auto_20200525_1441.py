# Generated by Django 3.0.5 on 2020-05-25 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hms', '0003_receptionist'),
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='receptionist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hms.Receptionist'),
        ),
    ]