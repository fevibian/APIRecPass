from django.urls import path
from .import views

urlpatterns = [
    path('verificar-email/<str:email>/', views.verificar_email, name='verificar-email'),
    path('cambiar-pass/<int:pk>/', views.cambiar_pass, name='cambiar-pass'),
]