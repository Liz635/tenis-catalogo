from django.shortcuts import render, get_object_or_404, redirect
from .models import Categoria, Producto, Pedido
from django import forms

# Formulario para el pedido
class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['nombre_cliente', 'telefono', 'direccion', 'email', 'notas']
        widgets = {
            'nombre_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre completo'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono / WhatsApp'}),
            'direccion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Dirección completa'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email (opcional)'}),
            'notas': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Notas (opcional)'}),
        }

# Página principal
def home(request):
    categorias = Categoria.objects.all()
    return render(request, 'catalogo/home.html', {'categorias': categorias})

# Detalle de categoría
def categoria_detail(request, slug):
    categoria = get_object_or_404(Categoria, slug=slug)
    productos = categoria.productos.all()
    return render(request, 'catalogo/categoria_detail.html', {
        'categoria': categoria,
        'productos': productos
    })

# Comprar producto
def comprar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.producto = producto
            pedido.save()
            return redirect('catalogo:exito_pedido')
    else:
        form = PedidoForm()
    
    return render(request, 'catalogo/comprar.html', {
        'producto': producto,
        'form': form
    })

# Éxito
def exito_pedido(request):
    return render(request, 'catalogo/exito.html')