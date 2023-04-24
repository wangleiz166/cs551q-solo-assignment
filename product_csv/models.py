from django.conf import settings
from django.db import models
from django.utils import timezone


class Product(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    product_id = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    date = models.DateField()
    img_link = models.CharField(max_length=255)
    product_link = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product'


class Review(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    product_id = models.CharField(max_length=255, null=True, blank=True)
    user_id = models.TextField()
    content = models.TextField()
    rating =  models.TextField()
    create_time = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'review'

