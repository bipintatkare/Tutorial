from django.contrib import admin
from .models import Category, Product
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ["product_name", "product_price", "product_category"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ["category_name"]