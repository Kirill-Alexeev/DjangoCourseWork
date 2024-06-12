from django.contrib import admin
from .models import Cake, Order, Client, Review, Image

# Register your models here.

class OrderInline(admin.TabularInline):
    """Определяет формат встроенной вставки заказа (используется в ClientAdmin)"""

    model = Order
    extra = 0


@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = ('title', 'weight', 'description', 'price')
    fields = ['id', 'title', 'weight', 'description', 'image_id', 'price', ('created_at', 'updated_at')]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_id', 'execution_date', 'status', 'comment', 'cost')
    fields = ['id', 'client_id', 'execution_date', 'status', 'comment', 'cost', 'cake', ('created_at', 'updated_at')]


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name', 'phone_number', 'email', 'date_of_birth')
    fields = ['id', 'first_name', 'middle_name', 'last_name', 'phone_number', 'email', 'date_of_birth', ('created_at', 'updated_at')]
    inlines = [OrderInline]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review', 'client_id', 'cake_id', 'image_id')
    fields = ['id', 'client_id', 'cake_id', 'image_id', 'review', 'created_at']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'alt', 'path')
    fields = ['id', 'alt', 'path', 'created_at']