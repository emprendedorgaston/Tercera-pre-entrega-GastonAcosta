from django.urls import path
from .views import CustomLoginView, CustomLogoutView, registro

urlpatterns = [
    path('registro/', registro, name='registro'),
    path('login/', CustomLoginView.as_view(), name='inicio_sesion'),
    path('logout/', CustomLogoutView.as_view(), name='cerrar_sesion'),
]
