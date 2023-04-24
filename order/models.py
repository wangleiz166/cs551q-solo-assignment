from django.db import models
from product_csv.models import Product


# CREATE TABLE order (
#     id INTEGER PRIMARY KEY,
#     purchase_time DATETIME NOT NULL,
#     buyer_name VARCHAR(50) NOT NULL,
#     buyer_email VARCHAR(50) NOT NULL,
#     buyer_address VARCHAR(100) NOT NULL,
#     buyer_phone VARCHAR(20) NOT NULL,
#     product_id INTEGER NOT NULL,
#     product_name VARCHAR(100) NOT NULL,
#     product_price DECIMAL(8, 2) NOT NULL
# );
class Order(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.name} ordered {self.quantity} {self.product.name}(s)'
    
    class Meta:
        db_table = 'order'

# CREATE TABLE cart (
#     id INTEGER PRIMARY KEY,
#     user_id INTEGER NOT NULL,
#     product_id INTEGER NOT NULL,
#     product_name VARCHAR(100) NOT NULL,
#     product_price DECIMAL(8, 2) NOT NULL,
#     product_quantity INTEGER NOT NULL
# );
class Cart(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=8, decimal_places=2)
    product_quantity = models.IntegerField()

    def __str__(self):
        return f'{self.user.name} has {self.product_quantity} {self.product.name}(s) in cart'
    class Meta:
        db_table = 'cart'     