from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('show_emp/', views.show_emp),
    path('show_proj/', views.show_proj),
    path('show_ben_emp/', views.show_ben_emp),
    path('addproject/',views.addproject),
    path('addemp/',views.addemp),    
    path('update_emp/<int:id>', views.update_emp),
    path('delete_emp/<int:id>', views.delete_emp),
    path('update_proj/<int:id>', views.update_proj),
    path('delete_proj/<int:id>', views.delete_proj),
]