from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('producto/<int:producto_id>/editar/', views.editar_producto, name='editar_producto'),
    path('categoria/agregar/', views.agregar_categoria, name='agregar_categoria'),
    path('buscar/', views.buscar_producto, name='buscar_producto'),
]
