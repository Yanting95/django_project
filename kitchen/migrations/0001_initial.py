# Generated by Django 2.2.5 on 2019-09-09 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kitchen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=100)),
                ('day', models.CharField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')], max_length=8)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='kitchen')),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('veg', models.BooleanField()),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Euro amount')),
                ('image', models.ImageField(blank=True, null=True, upload_to='kitchen')),
                ('kitchen', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='kitchen.Kitchen')),
            ],
        ),
    ]
