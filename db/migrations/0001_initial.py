# Generated by Django 2.2.7 on 2019-11-29 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OilField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Месторождение')),
                ('type', models.CharField(max_length=100, verbose_name='Тип')),
                ('location', models.CharField(max_length=100, verbose_name='Расположение')),
                ('owner', models.CharField(max_length=100, verbose_name='Недропользователь')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('obzor_img', models.ImageField(blank=True, upload_to='maps', verbose_name='Обзорная карта')),
            ],
        ),
        migrations.CreateModel(
            name='Well',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('type', models.CharField(blank=True, max_length=100, null=True)),
                ('altitude', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('x', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('y', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('md', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wells', to='db.OilField')),
            ],
            options={
                'unique_together': {('name', 'field')},
            },
        ),
    ]