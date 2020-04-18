from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:obj_id>', views.delete_todo, name='delete_todo'),
    path('display/', views.display, name='display'),
    path('activities-chart/', views.activities_chart, name='activities-chart')
]