from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from .forms import RegisterUserForm
from .models import Cake, Ingredient, Image, Order, Review, Client
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.

def index(request):
    """Функция отображения для домашней страницы сайта."""

    # Отрисовка HTML-шаблона index.html
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


# Регистрация пользователя

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'catalog/register.html'
    success_url = reverse_lazy('login')
 
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))


# Отзывы

class ReviewCreate(CreateView):
    model = Review
    fields = ['client_id', 'cake_id', 'image_id', 'review', 'created_at']
    success_url = reverse_lazy('reviews')


class ReviewUpdate( UpdateView):
    model = Review
    fields = ['client_id', 'cake_id', 'image_id', 'review']
    success_url = reverse_lazy('reviews')


class ReviewDelete(DeleteView):
    model = Review
    success_url = reverse_lazy('reviews')

    def form_valid(self, form):
        try:
            self.object.delete()
            return HttpResponseRedirect(self.success_url)
        except Exception as e:
            return HttpResponseRedirect(
                reverse("review-delete", kwargs={"pk": self.object.pk})
            )
        

# Заказы

class OrderCreate(PermissionRequiredMixin, CreateView):
    model = Order
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
    initial = {'date_of_death': '11/11/2023'}
    permission_required = 'catalog.add_order'


class OrderUpdate(PermissionRequiredMixin, UpdateView):
    model = Order
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
    permission_required = 'catalog.change_order'


class OrderDelete(PermissionRequiredMixin, DeleteView):
    model = Order
    success_url = reverse_lazy('orders')
    permission_required = 'catalog.delete_order'

    def form_valid(self, form):
        try:
            self.object.delete()
            return HttpResponseRedirect(self.success_url)
        except Exception as e:
            return HttpResponseRedirect(
                reverse("order-delete", kwargs={"pk": self.object.pk})
            )