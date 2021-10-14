from .models import Product
from .serializers import ProductSerializers
from rest_framework import viewsets

class ProductsViewSets(viewsets.ModelViewSet):
    #viewsets funciona como una vista normal pero NO renderiza template, devuelve json.
    queryset = Product.objects.all()
    #model necesario oara serializar (viewsets.ModelViewSet)
    serializer_class = ProductSerializers
    #serializa a json la respuesta
