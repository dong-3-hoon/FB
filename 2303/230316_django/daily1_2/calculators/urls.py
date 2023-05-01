from django.urls import path
from . import views
app_name='caltualtions'
urlpatterns=[
    path('calculation/', views.calculation, name='calculation'),
    path('result/', views.result, name='result'),
]