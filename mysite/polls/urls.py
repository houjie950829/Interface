from django.urls import path
from .import views

urlpatterns = [
    path('get_report/', views.get_report),
    path('report/', views.report),
]