# Generated by Django 3.0.3 on 2020-02-24 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0003_auto_20200224_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='contract_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
    ]
