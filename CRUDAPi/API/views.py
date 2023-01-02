from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from . models import Product
from . serializers import ProductSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def product_list(request):

    if request.method == 'GET': # get a list of all Products
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)