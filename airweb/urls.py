
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('book/', views.BookPage.as_view(), name='book'),
    path('about/', views.AboutPage.as_view(), name='about'),
    path('contact/', views.ContactPage.as_view(), name='contact'),
    path('book/thanks/', views.Thanks.as_view(), name='thanks'),
    path('contact/congrats/', views.Congrats.as_view(), name='congrats'),
]