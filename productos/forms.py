from django import forms
from .models import Categoria, Producto, Inventario

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'categoria']

class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['producto', 'cantidad']

class BuscarProductoForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=False)
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), required=False)
