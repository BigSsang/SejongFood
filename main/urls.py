from django.urls import path
from . import views

urlpatterns = [
    # path('sejong/', main_views.sejong, name='sejong'),
    path('search/', views.search, name='search'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('cate/', views.cate, name='cate'),
]