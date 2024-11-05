# Generated by Django 4.2 on 2024-11-03 05:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_vehicle_loan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Life_Insurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField(default=0)),
                ('Policy_holder_name', models.CharField(max_length=50)),
                ('Policy_number', models.IntegerField(default=0)),
                ('Company', models.CharField(default='', max_length=100)),
                ('starting_date', models.DateField(default=datetime.date.today)),
                ('term', models.CharField(default='', max_length=100)),
                ('premium', models.IntegerField(default=0)),
                ('sum_assured', models.IntegerField(default=0)),
                ('nominee_name', models.CharField(default='', max_length=100)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.customer')),
            ],
        ),
    ]