from django.urls import path

from . import views

urlpatterns = [
    path('search', views.search_user, name='search_user'),
    path('get_user/<str:pk>', views.get_user_by_id, name='get_user_by_id'),
]
