from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<usuario>/', views.getPersona, name="getPersona"),
    path('update/<usuario>/', views.updatePersona, name="updatePersona")
]