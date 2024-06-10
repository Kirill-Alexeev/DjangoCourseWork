# Generated by Django 5.0.6 on 2024-06-10 19:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.IntegerField(help_text='Уникальный ID для клиента', primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(help_text='Номер телефона клиента в формате: 89001230045', max_length=11)),
                ('email', models.EmailField(help_text='Электронная почта клиента', max_length=254)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('created_at', models.DateField(blank=True, null=True)),
                ('updated_at', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['last_name', 'first_name', 'middle_name'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.IntegerField(help_text='Уникальный ID для картинки', primary_key=True, serialize=False)),
                ('alt', models.CharField(help_text='Альтернативное расписание для картинки', max_length=100)),
                ('path', models.CharField(help_text='Путь до картинки', max_length=200)),
                ('created_at', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('id', models.IntegerField(help_text='Уникальный ID для торта', primary_key=True, serialize=False)),
                ('title', models.CharField(help_text='Название торта', max_length=200)),
                ('weight', models.CharField(help_text='Вес торта в граммах', max_length=10)),
                ('description', models.TextField(help_text='Описание для торта', max_length=1000)),
                ('price', models.CharField(help_text='Цена торта в рублях', max_length=10)),
                ('created_at', models.DateField(blank=True, null=True)),
                ('updated_at', models.DateField(blank=True, null=True)),
                ('image_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.image')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.IntegerField(help_text='Уникальный ID для заказа', primary_key=True, serialize=False)),
                ('execution_date', models.DateField(blank=True, help_text='Дата оформления заказа', null=True)),
                ('status', models.CharField(blank=True, choices=[('p', 'Preparation'), ('f', 'Finished')], default='p', help_text='Статус заказа', max_length=1)),
                ('comment', models.TextField(help_text='Комментарий к заказу', max_length=400)),
                ('cost', models.CharField(help_text='Стоимость заказа в рублях', max_length=10)),
                ('created_at', models.DateField(blank=True, null=True)),
                ('updated_at', models.DateField(blank=True, null=True)),
                ('cake', models.ManyToManyField(help_text='Выберите торт', to='catalog.cake')),
                ('client_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.client')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.IntegerField(help_text='Уникальный ID для отзыва', primary_key=True, serialize=False)),
                ('review', models.TextField(help_text='Отзыв к заказу', max_length=1000)),
                ('created_at', models.DateField(blank=True, null=True)),
                ('cake_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.cake')),
                ('client_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.client')),
                ('image_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.image')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
