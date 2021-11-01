from rest_framework import serializers
from .models import Product

class ProductSerializers(serializers.ModelSerializer):

    class Meta:
        model= Product
        exclude = ['created', 'updated'] # para excluir campo
        #fields = "__all__"
#fields=["name","price"]
#exluide=["created", "update"] 
#o uno o el otro.
