from .serializers import StoreSerializer, ProductCategorySerializer, \
    ProductSerializerPost, ProductSerializer, PutProductSerializer

from .models import Store, ProductCategory, Product
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from drf_yasg.utils import swagger_auto_schema


class StoreList(generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class StoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductList(APIView):
    def get(self, request, store_id, category_id, format=None):
        products = Product.objects.filter(store=store_id, category=category_id)
        serializer = ProductSerializerPost(products, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ProductSerializerPost)
    def post(self, request, store_id, category_id, format=None):
        data = JSONParser().parse(request)
        if isinstance(data, list):
            for obj in data:
                obj['store'] = store_id
                obj['category'] = category_id
                serializer = ProductSerializer(data=data, many=True)
        else:
            data['store'] = store_id
            data['category'] = category_id
            serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)


class ProductDetail(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except ProductCategory.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, store_id, category_id, product_id, format=None):
        product = self.get_object(product_id)
        serializer = ProductSerializerPost(product)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=PutProductSerializer)
    def put(self, request, store_id, category_id, product_id, format=None):
        product = self.get_object(product_id)
        data = request.data
        serializer = ProductSerializer(product, data=data)
        if serializer.is_valid():
            serializer.update(product, data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
