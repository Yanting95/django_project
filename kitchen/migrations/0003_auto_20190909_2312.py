# Generated by Django 2.2.5 on 2019-09-10 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0002_auto_20190909_1629'),
    ]

    operations = [
        migrations.CreateModel(
            name='Days',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=8)),
            ],
        ),
        migrations.RemoveField(
            model_name='kitchen',
            name='day',
        ),
        migrations.AddField(
            model_name='kitchen',
            name='days',
            field=models.ManyToManyField(default='', to='kitchen.Days'),
        ),
    ]