from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Главная страница
    path('add/', views.add_entry, name='add_entry'),  # Страница добавления записи
    # другие маршруты...
]

from django.urls import path
from .views import index, add_entry, entry_detail

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_entry, name='add_entry'),
    path('entry/<int:entry_id>/', entry_detail, name='entry_detail'),
]
    