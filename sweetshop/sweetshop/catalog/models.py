from django.db import models
from django.urls import reverse

# Create your models here.

class Cake(models.Model):
    '''Модель представляющая торты'''

    id = models.IntegerField(primary_key=True, help_text="Уникальный ID для торта")
    title = models.CharField(max_length=200, help_text="Название торта")
    weight = models.CharField(max_length=10, help_text="Вес торта в граммах")
    description = models.TextField(max_length=2000, help_text="Описание для торта")
    image_id = models.ForeignKey("Image", on_delete=models.SET_NULL, null=True)
    price = models.CharField(max_length=10, help_text="Цена торта в рублях")
    ingredient = models.ManyToManyField('Ingredient', help_text="Выберите ингредиенты")
    created_at = models.DateField(null=True, blank=True)
    updated_at = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        '''Строка для представления объекта модели'''

        return self.title

    def get_absolute_url(self):
        '''Возвращает url для доступа к определённому торту'''
        
        return reverse("cake-detail", args=[str(self.id)])


class Order(models.Model):
    '''Модель представляющая заказы'''

    id = models.IntegerField(primary_key=True, help_text="Уникальный ID для заказа")
    client_id = models.ForeignKey("Client", on_delete=models.SET_NULL, null=True)
    execution_date = models.DateField(null=True, blank=True, help_text="Дата оформления заказа")
    
    LOAN_STATUS = [
        ("p", "Preparation"),
        ("f", "Finished"),
    ]
    
    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default="p",
        help_text="Статус заказа",
    )
    comment = models.TextField(max_length=400, help_text="Комментарий к заказу")
    cost = models.CharField(max_length=10, help_text="Стоимость заказа в рублях")
    cake = models.ManyToManyField('Cake', help_text="Выберите торт")
    created_at = models.DateField(null=True, blank=True)
    updated_at = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        '''Строка для представления объекта модели'''

        return str(self.id)

    def get_absolute_url(self):
        '''Возвращает url для доступа к определённому заказу'''
        
        return reverse("order-detail", args=[str(self.id)])


class Client(models.Model):
    '''Модель представляющая клиентов'''

    id = models.IntegerField(primary_key=True, help_text="Уникальный ID для клиента")
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11, help_text='Номер телефона клиента в формате: 89001230045')
    email = models.EmailField(help_text="Электронная почта клиента")
    date_of_birth = models.DateField(null=True, blank=True)
    created_at = models.DateField(null=True, blank=True)
    updated_at = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["last_name", "first_name", "middle_name"]

    def __str__(self):
        '''Строка для представления объекта модели'''

        return f"{self.last_name}, {self.first_name} {self.middle_name}"

    def get_absolute_url(self):
        '''Возвращает url для доступа к определённому клиенту'''
        
        return reverse("client-detail", args=[str(self.id)])


class Review(models.Model):
    '''Модель представляющая отзывы клиентов'''

    id = models.IntegerField(primary_key=True, help_text="Уникальный ID для отзыва")
    client_id = models.ForeignKey("Client", on_delete=models.SET_NULL, null=True)
    cake_id = models.ForeignKey("Cake", on_delete=models.SET_NULL, null=True)
    image_id = models.ForeignKey("Image", on_delete=models.SET_NULL, null=True)
    review = models.TextField(max_length=1000, help_text="Отзыв к заказу")
    created_at = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        '''Строка для представления объекта модели'''

        return str(self.id)

    def get_absolute_url(self):
        '''Возвращает url для доступа к определённому отзыву'''
        
        return reverse("review-detail", args=[str(self.id)])


class Image(models.Model):
    '''Модель представляющая изображения'''

    id = models.IntegerField(primary_key=True, help_text="Уникальный ID для картинки")
    alt = models.CharField(max_length=100, help_text="Альтернативное расписание для картинки")
    path = models.CharField(max_length=200, help_text="Путь до картинки")
    created_at = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        '''Строка для представления объекта модели'''

        return self.alt


class Ingredient(models.Model):
    '''Модель представляющая ингредиенты для тортов'''

    id = models.IntegerField(primary_key=True, help_text="Уникальный ID для ингредиента")
    title = models.CharField(max_length=200, help_text="Название ингредиента")
    units = models.CharField(max_length=50, help_text="Название единиц измерения")
    count = models.IntegerField(help_text="Количество ингредиента")
    created_at = models.DateField(null=True, blank=True)
    updated_at = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        '''Строка для представления объекта модели'''

        return self.title
    
    def get_absolute_url(self):
        '''Возвращает url для доступа к определённому ингредиенту'''
        
        return reverse("ingredient-detail", args=[str(self.id)])