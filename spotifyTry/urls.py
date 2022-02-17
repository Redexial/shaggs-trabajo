from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<usuario>/', views.userPersona, name="userPersona"),
    path('update/<usuario>/', views.updatePersona, name="updatePersona"),
    path('create/<usuario>/', views.createPersona, name="createPersona")
]