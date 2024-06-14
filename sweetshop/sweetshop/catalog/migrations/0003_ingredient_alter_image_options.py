# Generated by Django 5.0.6 on 2024-06-14 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_cake_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.IntegerField(help_text='Уникальный ID для ингредиента', primary_key=True, serialize=False)),
                ('title', models.CharField(help_text='Название ингредиента', max_length=200)),
                ('units', models.CharField(help_text='Название единиц измерения', max_length=50)),
                ('count', models.IntegerField(help_text='Количество ингредиента')),
                ('created_at', models.DateField(blank=True, null=True)),
                ('updated_at', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['id']},
        ),
    ]
