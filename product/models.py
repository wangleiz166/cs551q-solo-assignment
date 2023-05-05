from django.db import models
from product_csv.models import Product as CsvProduct

# CREATE TABLE payment (
#     id INTEGER PRIMARY KEY,
#     user_id INTEGER NOT NULL,
#     order_id INTEGER NOT NULL,
#     payment_method VARCHAR(50) NOT NULL,Q
#     payment_amount DECIMAL(8, 2) NOT NULL,
#     payment_time DATETIME NOT NULL
# );
class Payment(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    product = models.ForeignKey(CsvProduct, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.name} paid {self.amount} for {self.product.name} at {self.payment_time}'
    class Meta:
        db_table = 'payment'