from django.urls import path
from scraper import views

urlpatterns = [
    path('', views.index, name='home'),
    path('result/<str:task_id>', views.check_result, name='check_result'),
]