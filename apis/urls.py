from django.urls import path

from .views import GetUser


urlpatterns = [
    path('get_user/<str:email>', GetUser.as_view()),
]
