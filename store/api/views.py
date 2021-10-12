from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .serializers import StoreSerializer, ProductCategorySerializer, ProductSerializerPostman, ProductSerializer, \
    PutProductSerializer
from .models import Store, ProductCategory, Product

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from drf_yasg.utils import swagger_auto_schema


class StoreList(APIView):
    def get(self, request, format=None):
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(operation_description="description", request_body=StoreSerializer)
    def post(self, request, format=None):
        serializer = StoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StoreDetail(APIView):
    def get_object(self, pk):
        try:
            return Store.objects.get(pk=pk)
        except Store.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk, format=None):
        store = self.get_object(pk)
        serializer = StoreSerializer(store)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=StoreSerializer)
    def put(self, request, pk, format=None):
        store = self.get_object(pk)
        serializer = StoreSerializer(store, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        store = self.get_object(pk)
        store.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@swagger_auto_schema(method='POST', request_body=ProductCategorySerializer)
@api_view(['POST'])
def add_product_category(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductCategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)


@csrf_exempt
@api_view(['GET'])
def product_categories_list(request, store_id):
    if request.method == 'GET':
        categories = ProductCategory.objects.filter(store=store_id)
        serializer = ProductCategorySerializer(categories, many=True)
        return JsonResponse(serializer.data, safe=False)


class ProductCategoryDetail(APIView):
    def get_object(self, pk):
        try:
            return ProductCategory.objects.get(pk=pk)
        except ProductCategory.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = ProductCategorySerializer(category)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ProductCategorySerializer)
    def put(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = StoreSerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@swagger_auto_schema(method='POST', request_body=ProductSerializerPostman)
@api_view(['GET', 'POST'])
def product_list(request, store_id, category_id):
    if request.method == 'GET':
        products = Product.objects.filter(store=store_id, category=category_id)
        serializer = ProductSerializerPostman(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
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


class ProductList(APIView):
    def get(self, request, store_id, category_id, format=None):
        products = Product.objects.filter(store=store_id, category=category_id)
        serializer = ProductSerializerPostman(products, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ProductSerializerPostman)
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
        serializer = ProductSerializerPostman(product)
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
