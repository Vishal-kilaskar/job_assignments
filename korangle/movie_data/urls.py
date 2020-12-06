from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('api/get_data/', views.get_data),
    path('api/post_data/', views.post_data)
]