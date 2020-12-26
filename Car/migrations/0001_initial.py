# Generated by Django 3.1.4 on 2020-12-20 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('price', models.PositiveSmallIntegerField()),
                ('year', models.PositiveSmallIntegerField()),
                ('casco', models.BooleanField()),
                ('osago', models.BooleanField()),
                ('max_limit', models.PositiveSmallIntegerField()),
                ('mileage', models.PositiveIntegerField()),
                ('color', models.CharField(max_length=20)),
                ('number', models.CharField(max_length=10)),
                ('photo', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Car_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gearbox', models.CharField(max_length=15)),
                ('body', models.CharField(max_length=15)),
                ('seats', models.PositiveSmallIntegerField()),
                ('drive', models.CharField(max_length=10)),
                ('engine', models.CharField(max_length=10)),
                ('doors', models.PositiveSmallIntegerField()),
                ('rudder', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Deliveryman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('profile', models.CharField(max_length=10)),
                ('photo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('metro', models.CharField(max_length=30)),
                ('street', models.CharField(max_length=100)),
                ('building', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_birth', models.DateField()),
                ('gender', models.CharField(blank=True, max_length=1)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('photo', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_rent', models.CharField(max_length=8)),
                ('delivery_location', models.CharField(max_length=100)),
                ('time', models.DateTimeField()),
                ('price', models.PositiveSmallIntegerField()),
                ('deliveryman_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Car.deliveryman')),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Car.location')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Car.user')),
            ],
        ),
        migrations.CreateModel(
            name='Car_rent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('region', models.CharField(max_length=40)),
                ('limit', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('comment', models.CharField(blank=True, max_length=200)),
                ('car_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Car.car')),
                ('delivery_from_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='deliveryfromcar', to='Car.delivery')),
                ('delivery_to_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Car.delivery')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Car.user')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='car_model_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Car.car_model'),
        ),
        migrations.AddField(
            model_name='car',
            name='location_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Car.location'),
        ),
    ]