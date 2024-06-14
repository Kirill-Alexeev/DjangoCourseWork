from django.shortcuts import render
from .models import Cake, Ingredient, Image, Order, Review, Client
from django.views import generic

# Create your views here.

def index(request):
    """Функция отображения для домашней страницы сайта."""

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        "index.html",
        context={},
    )

class CakeListView(generic.ListView):
    model = Cake
    paginate_by = 9


class CakeDetailView(generic.DetailView):
    model = Cake


class ReviewListView(generic.ListView):
    model = Review
    paginate_by = 9


class ReviewDetailView(generic.DetailView):
    model = Review

