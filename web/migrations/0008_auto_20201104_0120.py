# Generated by Django 3.1.1 on 2020-11-04 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20201104_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insumo',
            name='imagen',
            field=models.ImageField(null=True, upload_to='Insumo'),
        ),
    ]
