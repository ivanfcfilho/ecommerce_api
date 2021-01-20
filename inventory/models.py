from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=128)
    street = models.CharField(max_length=256)
    number = models.IntegerField()
    neighborhood = models.CharField(max_length=32)
    country = models.CharField(max_length=16)
    state = models.CharField(max_length=2)
    zipcode = models.IntegerField()


class Department(models.Model):
    name = models.CharField(max_length=128)


class Category(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    department = models.ForeignKey(
        "Department", related_name="department", on_delete=models.CASCADE
    )


class SubCategory(models.Model):
    name = models.CharField(max_length=64)
    category = models.ForeignKey(
        "Category", related_name="category", on_delete=models.CASCADE
    )


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    sub_category = models.ForeignKey(
        "SubCategory", related_name="sub_category", on_delete=models.CASCADE
    )
    thumbnail = models.ImageField(width_field=800, height_field=1098)
    image = models.ImageField(width_field=800, height_field=1098)
    thumbnail_image = models.ImageField(width_field=180, height_field=180)


class StoreProductDetail(models.Model):

    store = models.ForeignKey("Store", related_name="store", on_delete=models.CASCADE)
    product = models.ForeignKey(
        "Product", related_name="product", on_delete=models.CASCADE
    )
    price = models.DecimalField(decimal_places=2, max_digits=8)
