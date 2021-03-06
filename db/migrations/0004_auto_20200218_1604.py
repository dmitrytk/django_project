# Generated by Django 3.0.2 on 2020-02-18 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_auto_20200217_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='well',
            name='alt',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='well',
            name='md',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='well',
            name='x',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='well',
            name='y',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True),
        ),
    ]
