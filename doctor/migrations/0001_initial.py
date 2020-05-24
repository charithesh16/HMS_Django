# Generated by Django 3.0.5 on 2020-05-24 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hms', '0002_auto_20200524_0821'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(default=None, max_length=10)),
                ('gender', models.CharField(default=None, max_length=10)),
                ('age', models.IntegerField(default=None)),
                ('address', models.CharField(default=None, max_length=256)),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hms.Person')),
            ],
        ),
    ]
