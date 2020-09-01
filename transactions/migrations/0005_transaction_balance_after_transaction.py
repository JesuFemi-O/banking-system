# Generated by Django 3.1 on 2020-09-01 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0004_auto_20200901_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='balance_after_transaction',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=12),
            preserve_default=False,
        ),
    ]
