# Generated by Django 4.2 on 2024-11-02 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_documents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='card_num',
            field=models.CharField(default='', max_length=100),
        ),
    ]
