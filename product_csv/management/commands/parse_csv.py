import csv
import datetime
import uuid
from pathlib import Path
from django.core.management.base import BaseCommand
from product_csv.models import Product, Review

class Command(BaseCommand):
    help = 'Load data from csv'

    def handle(self, *args, **options):
        # delete existing data
        Product.objects.all().delete()
        print("Table Product dropped successfully")
        Review.objects.all().delete()
        print("Table Review dropped successfully")

        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(str(base_dir) + '/product_csv/shop_information/amazon.csv', newline='', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=",")
            try:
                # skip the header line
                next(reader)
            except StopIteration:
                # If the file is empty, print an error message and return
                print("Error: CSV file is empty")
                return
            for row in reader:
                try:
                    # extract data from csv row
                    product_id = row[0]
                    product_name = row[1]
                    category = row[2]
                    discounted_price = row[3]
                    rating = row[6]
                    img_link = row[14]
                    product_link = row[15]
                    user_id = str(uuid.uuid4())
                    review_content = row[13]

                    # create Product object and save to database
                    product = Product(product_id=product_id, name=product_name, category=category, price=discounted_price,
                                      date=datetime.date.today(), img_link=img_link, product_link=product_link)
                    product.save()

                    # create Review object and save to database
                    create_time = datetime.datetime.now().strftime('%Y-%m-%d')
                    review = Review(product_id=product_id, user_id=user_id, rating=rating,
                                      content=review_content, create_time=create_time)
                    review.save()
                except Exception as e:
                    print(f"Error: Could not create record for row {reader.line_num}: {e}")
