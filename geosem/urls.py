from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='geosem-main'),
    path('map/', views.map_page, name='geosem-map'),
    path('info/', views.info_page, name='geosem-info'),
    path('about/', views.about_page, name='geosem-about')
]

