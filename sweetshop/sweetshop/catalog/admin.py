from django.contrib import admin
from .models import Cake, Order, Client, Review, Image, Ingredient

# Register your models here.

class OrderInline(admin.TabularInline):
    """Определяет формат встроенной вставки заказа (используется в ClientAdmin)"""

    model = Order
    extra = 0


class ReviewInline(admin.TabularInline):
    """Определяет формат встроенной вставки заказа (используется в ClientAdmin)"""

    model = Review
    extra = 0


@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'weight', 'description', 'created_at', 'brief_info')
    fields = ['id', 'title', 'weight', 'description', 'image_id', 'price', 'ingredient', ('created_at', 'updated_at')]
    readonly_fields = ('id',)
    list_filter = ('title', 'price')
    inlines = [ReviewInline]
    date_hierarchy = 'created_at'
    filter_horizontal = ('ingredient',)
    raw_id_fields = ('image_id',)
    search_fields = ('title',)
    list_per_page = 4

    @admin.display(description="Number of symbols", ordering='description')
    def brief_info(self, cake: Cake):
        return f"Описание {len(cake.description)} символов."


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_id', 'execution_date', 'status', 'comment', 'cost', 'created_at')
    list_display_links = ('id', 'client_id')
    fields = ['id', 'client_id', 'execution_date', 'status', 'comment', 'cost', 'cake', ('created_at', 'updated_at')]
    readonly_fields = ('id',)
    list_filter = ('status', 'execution_date')
    date_hierarchy = 'created_at'
    filter_horizontal = ('cake',)
    raw_id_fields = ('client_id',)
    search_fields = ('id',)
    list_per_page = 10


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name', 'phone_number', 'email', 'date_of_birth', 'created_at')
    list_display_links = ('last_name', 'first_name', 'middle_name')
    fields = ['id', 'first_name', 'middle_name', 'last_name', 'phone_number', 'email', 'date_of_birth', ('created_at', 'updated_at')]
    readonly_fields = ('id',)
    inlines = [OrderInline]
    date_hierarchy = 'created_at'
    search_fields = ('last_name', 'first_name', 'middle_name')
    list_per_page = 20


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review', 'client_id', 'cake_id', 'image_id', 'created_at')
    fields = ['id', 'client_id', 'cake_id', 'image_id', 'review', 'created_at']
    readonly_fields = ('id',)
    date_hierarchy = 'created_at'
    raw_id_fields = ('client_id', 'cake_id', 'image_id')
    search_fields = ('review',)
    list_per_page = 5


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'alt', 'path', 'created_at')
    list_display_links = ('id', 'alt')
    fields = ['id', 'alt', 'path', 'created_at']
    readonly_fields = ('id',)
    date_hierarchy = 'created_at'
    search_fields = ('id', 'alt')
    list_per_page = 20


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('title', 'count', 'units', 'created_at')
    fields = ['id', 'title', 'units', 'count', ('created_at', 'updated_at')]
    readonly_fields = ('id',)
    list_filter = ('title', 'units')
    date_hierarchy = 'created_at'
    search_fields = ('title',)
    list_per_page = 15