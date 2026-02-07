from django.db import models
from django.urls import reverse
from cloudinary.models import CloudinaryField


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    imagen = CloudinaryField('imagen', folder='categorias/', blank=True, null=True)

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('catalogo:categoria_detail', args=[self.slug])


class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = CloudinaryField('imagen', folder='productos/', blank=True, null=True)

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    nombre_cliente = models.CharField(max_length=200)
    telefono = models.CharField(max_length=50)
    direccion = models.TextField()
    email = models.EmailField(blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    notas = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre_cliente} - {self.producto.nombre}"