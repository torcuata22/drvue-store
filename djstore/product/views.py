from django.db.models import Q
from django.shortcuts import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer, CategorySerializer
from .models import Product, Category

class LatestProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductDetail(APIView):
    #check if product exists
    def get_object(self, category_slug, product_slug):  
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404

    #override get method
    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, format=None):
        print(category_slug)
        category = self.get_object(category_slug)
        print(f"Category: {category}")
        serializer = CategorySerializer(category)
        return Response(serializer.data)

#Search functionality (accept ONLY post requests, so use the decorator)
@api_view(['POST'])
def search(request):
    print(request.data)
    query = request.data.get('query', '')
    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query)) #filter based on name or description
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response(
            {"products": []}
        )