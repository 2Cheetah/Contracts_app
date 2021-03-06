# Generated by Django 3.0.3 on 2020-02-24 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0002_auto_20200224_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='contract_appendix1',
            field=models.FileField(blank=True, null=True, upload_to='contracts'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='contract_appendix2',
            field=models.FileField(blank=True, null=True, upload_to='contracts'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='contract_file_signed',
            field=models.FileField(blank=True, null=True, upload_to='contracts/signed'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='contract_specification',
            field=models.FileField(blank=True, null=True, upload_to='contracts'),
        ),
    ]
