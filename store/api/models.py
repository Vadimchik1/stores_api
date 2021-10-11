from django.db import models


# Create your models here.

class Store(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')


class ProductCategory(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    store = models.ForeignKey(Store, verbose_name='Магазин', on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(ProductCategory, verbose_name='Категория товара', on_delete=models.SET_NULL, null=True)
