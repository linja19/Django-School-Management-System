# Generated by Django 3.0.8 on 2020-11-24 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corecode', '0003_auto_20200726_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicsession',
            name='current',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='academicterm',
            name='current',
            field=models.BooleanField(default=True),
        ),
    ]