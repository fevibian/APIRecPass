from django.urls import path
from .import views

urlpatterns = [
    path('recpass/<str:email>', views.recPass, name="recpass"),
]