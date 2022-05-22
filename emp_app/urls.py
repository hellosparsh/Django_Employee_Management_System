
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index,name='emp_index'),
    path('all_emp/', views.all_emp,name='emp_all'),
    path('add_emp/', views.add_emp,name='emp_add'),
    path('remove_emp/', views.remove_emp,name='emp_remove'),
    path('remove_emp/<int:emp_id>', views.remove_emp,name='emp_remove'),
    path('filter_emp/', views.filter_emp,name='emp_filter'),
]