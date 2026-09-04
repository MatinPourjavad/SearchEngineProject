from django.urls import path
from . import views

urlpatterns = [
    path('api/search/', views.SearchAPIView.as_view(), name='api_search'),
    # path('', views.HomeView.as_view(), name='home_search'),
]