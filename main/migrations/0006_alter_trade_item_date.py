# Generated by Django 3.2.5 on 2022-12-15 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_trade_date_trade_item_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='item_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
