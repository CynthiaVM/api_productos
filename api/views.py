from rest_framework import permissions
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializers


class ProductsViewSets(viewsets.ModelViewSet):
    #viewsets funciona como una vista normal pero NO renderiza template, devuelve json.
    queryset = Product.objects.all()
    #model necesario oara serializar (viewsets.ModelViewSet)
    serializer_class = ProductSerializers
    #serializa a json la respuesta

    #permission_classes = [permissions.IsAuthenticated]