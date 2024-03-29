# Generated by Django 4.0.6 on 2022-07-14 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Benchemp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Benchemp_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_id', models.IntegerField()),
                ('Employee_name', models.CharField(max_length=30)),
                ('Employees_address', models.CharField(max_length=100)),
                ('Employee_phone_number', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Project_id', models.IntegerField()),
                ('Project_name', models.CharField(max_length=30)),
                ('Project_employees', models.CharField(max_length=100)),
            ],
        ),
    ]
