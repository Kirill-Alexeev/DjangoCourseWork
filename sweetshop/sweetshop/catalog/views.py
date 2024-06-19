import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required

from django.utils.dateparse import parse_date
from .forms import OrderForm, RegisterUserForm
from .models import Cake, Order, Review
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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
    paginate_by = 7


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
    fields = ['user_id', 'cake_id', 'image_id', 'review', 'created_at']
    success_url = reverse_lazy('reviews')


class ReviewUpdate( UpdateView):
    model = Review
    fields = ['user_id', 'cake_id', 'image_id', 'review']
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
        

# Корзина и оформление заказа

def cart(request, id):
    if 'cart' not in request.session:
        request.session['cart'] = {'items': [], 'total_price': 0}

    cake = get_object_or_404(Cake, id=id)

    if 'items' not in request.session['cart']:
        request.session['cart']['items'] = []
    if 'total_price' not in request.session['cart']:
        request.session['cart']['total_price'] = 0

    request.session['cart']['items'].append({
        'id': cake.id,
        'name': cake.title,
        'price': float(cake.price)
    })

    request.session['cart']['total_price'] += float(cake.price)
    request.session.modified = True  # Обязательно сохраняем изменения в сессии

    return HttpResponseRedirect(reverse('cart_view'))


@login_required
def cart_view(request):
    cart = request.session.get('cart', {'items': [], 'total_price': 0})

    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.user_id = request.user
            order.cost = cart['total_price']
            order.created_at = datetime.date.today()

            order.save()

            # Очистка корзины после оформления заказа
            request.session['cart'] = {'items': [], 'total_price': 0}

            return redirect('order_success')
    else:
        order_form = OrderForm()

    return render(request, 'catalog/cart.html', {
        'cart': cart,
        'order_form': order_form
    })
        

def order_success(request):
    return render(request, 'catalog/order_success.html')