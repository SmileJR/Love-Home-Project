from django.db import models


class Item(models.Model):
    type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    image_url = models.TextField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    items = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='category')

    def __str__(self):
        return self.name


class Cart(models.Model):
    total = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)
    items = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='cart')

    def __str__(self):
        return self.total


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_lentgh=255)
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    billing_address = models.CharField(max_length=255)
    billing_city = models.CharField(max_length=255)
    billing_state = models.CharField(max_length=255)
    billing_zip_code = models.CharField(max_length=255)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE, related_name='user', primary_key=True)

    def __str__(self):
        return self.name
