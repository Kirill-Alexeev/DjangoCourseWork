# Generated by Django 5.0.6 on 2024-06-14 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_ingredient_alter_image_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='cake',
            name='ingredient',
            field=models.ManyToManyField(help_text='Выберите ингредиенты', to='catalog.ingredient'),
        ),
    ]
