from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path(r"^$", views.index, name="index"),
    re_path(r"^cakes/$", views.CakeListView.as_view(), name="cakes"),
    re_path(r"^cake/(?P<pk>\d+)$", views.CakeDetailView.as_view(), name="cake-detail"),
    re_path(r"^reviews/$", views.ReviewListView.as_view(), name="reviews"),
    re_path(r"^review/(?P<pk>\d+)$", views.ReviewDetailView.as_view(), name="review-detail"),
]