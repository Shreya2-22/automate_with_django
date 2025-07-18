# Generated by Django 5.2.1 on 2025-06-30 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cereal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mfr', models.CharField(max_length=1)),
                ('type', models.CharField(max_length=1)),
                ('calories', models.IntegerField()),
                ('protein', models.FloatField()),
                ('fat', models.FloatField()),
                ('sodium', models.FloatField()),
                ('fiber', models.FloatField()),
                ('carbo', models.FloatField()),
                ('sugars', models.FloatField()),
                ('potass', models.FloatField()),
                ('vitamins', models.FloatField()),
                ('shelf', models.IntegerField()),
                ('weight', models.FloatField()),
                ('cups', models.FloatField()),
                ('rating', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'Cereals',
            },
        ),
    ]
