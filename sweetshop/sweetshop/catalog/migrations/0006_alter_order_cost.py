# Generated by Django 5.0.6 on 2024-06-17 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_cake_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
