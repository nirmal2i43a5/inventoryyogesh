# Generated by Django 3.1 on 2021-01-05 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0003_auto_20210105_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Quantity',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]