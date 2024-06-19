from django.test import TestCase
from django.contrib.auth.models import User
from catalog.models import Cake, Order, Review, Ingredient
from django.urls import reverse
from datetime import date

# Create your tests here.

class CatalogTests(TestCase):

    def setUp(self):
        # Создаем тестового пользователя
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        # Создаем тестовый ингредиент
        self.ingredient = Ingredient.objects.create(title='Sugar', count='12', units='кг')
        
        # Создаем тестовый торт
        self.cake = Cake.objects.create(title='Test Cake', price=10.0)

        # Создаем тестовый заказ
        self.order = Order.objects.create(
            user_id=self.user,
            execution_date=date.today(),
            comment='Test order',
            delivery_address='123 Test St',
            cost=100.0
        )
        
        # Создаем тестовый отзыв
        self.review = Review.objects.create(
            user_id=self.user,
            cake_id=self.cake,
            review='Great cake!'
        )

    def test_cake_creation(self):
        self.assertEqual(self.cake.name, 'Test Cake')
        self.assertEqual(self.cake.price, 10.0)
        self.assertIn(self.ingredient, self.cake.ingredients.all())

    def test_order_creation(self):
        self.assertEqual(self.order.user, self.user)
        self.assertEqual(self.order.execution_date, date.today())
        self.assertEqual(self.order.comment, 'Test order')
        self.assertEqual(self.order.delivery_address, '123 Test St')
        self.assertEqual(self.order.cost, 100.0)
        self.assertIn(self.cake, self.order.cake.all())

    def test_review_creation(self):
        self.assertEqual(self.review.user, self.user)
        self.assertEqual(self.review.cake, self.cake)
        self.assertEqual(self.review.rating, 5)
        self.assertEqual(self.review.comment, 'Great cake!')

    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/register.html')

    def test_cart_view(self):
        self.client.login(username='testuser', password='testpassword')
        session = self.client.session
        session['cart'] = {'items': [{'id': self.cake.id}], 'total_price': 10.0}
        session.save()

        response = self.client.get(reverse('cart'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/cart.html')

    def test_order_success_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('order_success'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/order_success.html')

    def test_add_cake_to_order(self):
        self.client.login(username='testuser', password='testpassword')
        session = self.client.session
        session['cart'] = {'items': [{'id': self.cake.id}], 'total_price': 10.0}
        session.save()

        response = self.client.post(reverse('cart'), {
            'execution_date': date.today(),
            'comment': 'Test order',
            'delivery_address': '123 Test St'
        })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('order_success'))

        order = Order.objects.get(comment='Test order')
        self.assertEqual(order.user, self.user)
        self.assertEqual(order.cost, 10.0)
        self.assertIn(self.cake, order.cake.all())