from django.urls import path
from . import views

app_name = 'catalogo'

urlpatterns = [
    path('', views.home, name='home'),
    path('categoria/<slug:slug>/', views.categoria_detail, name='categoria_detail'),
    path('comprar/<int:producto_id>/', views.comprar_producto, name='comprar_producto'),  # ← esta línea
    path('exito/', views.exito_pedido, name='exito_pedido'),  # ← esta línea
]