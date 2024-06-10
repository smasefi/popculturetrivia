from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login2'),
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('categories/', views.categories, name='categories'),
    path('categories/<int:category_id>/', views.category_questions, name='category_questions'),
]
