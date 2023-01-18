from django.db import models

# Create your models here.

class Blog(models.Model):

    title = models.CharField(max_length=100, default="")
    description = models.TextField(default="")

    def __str__(self):
        return self.title


class Category(models.Model):

    category_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):

    # VARCHAR max_length to store characters is 256 (0 to 255)
    product_name = models.CharField(max_length=255, default="")
    product_image = models.ImageField(upload_to='product/', null=True, blank=True)
    product_price = models.FloatField(default=0.0)
    product_description = models.TextField()
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name