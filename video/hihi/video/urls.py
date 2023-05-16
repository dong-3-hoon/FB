from django.urls import path, include
from . import views
app_name='video'
urlpatterns = [
    path('', views.video_list),
    path('new/', views.video_new),
    path('<video_id>/', views.video_detail),
]