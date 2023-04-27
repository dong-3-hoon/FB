from . import views
from django.urls import path

app_name = 'myapp2'
urlpatterns = [
    path("hello/<name>/", views.hello, name="hello"),
]