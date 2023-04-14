from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path ('project/<str:name>/', views.project, name='project'),
]