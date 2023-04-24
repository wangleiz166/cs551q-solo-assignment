from django.db import models


# CREATE TABLE user (
#     id INTEGER PRIMARY KEY,
#     username VARCHAR(50) NOT NULL,
#     password VARCHAR(50) NOT NULL,
#     email VARCHAR(50) NOT NULL,
#     recipient_name VARCHAR(50) NOT NULL,
#     province VARCHAR(50) NOT NULL,
#     city VARCHAR(50) NOT NULL,
#     district VARCHAR(50) NOT NULL,
#     address VARCHAR(100) NOT NULL,
#     phone VARCHAR(20) NOT NULL
# );
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'user'