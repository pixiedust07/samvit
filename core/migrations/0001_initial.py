# Generated by Django 4.1 on 2022-08-10 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('number_of_slot', models.IntegerField(default=0)),
                ('time', models.CharField(choices=[('10:00 AM', '10:00 AM'), ('11:00 AM', '11:00 AM'), ('12:00 AM', '12:00 AM'), ('01:00 PM', '01:00 PM'), ('02:00 PM', '02:00 PM'), ('03:00 PM', '03:00 PM'), ('04:00 PM', '04:00 PM'), ('05:00 PM', '05:00 PM')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('e_id', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Colleges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.reservation')),
            ],
        ),
    ]
