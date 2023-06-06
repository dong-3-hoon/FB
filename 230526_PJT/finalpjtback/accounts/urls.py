from django.urls import path
from . import views
from dj_rest_auth.views import PasswordChangeView

urlpatterns = [
    path("userinfo/", views.userinfo),
    path('<int:user_pk>/follow/', views.follow, name='follow'),
    # path('signup/<int:user_pk>', views.signup)
    path('update/', views.update),
    path('update/nickname/', views.update_nickname),
    path('password/change/', PasswordChangeView.as_view()),
    path('follow/<int:user_pk>/', views.follow),
    # path('update_profile/', views.update_profile),
]