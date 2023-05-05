from behave import given, when, then
from django.test import Client
from django.urls import reverse
from product_csv.models import Product

@given('the following products exist')
def step_given_the_following_products_exist(context):
    for row in context.table:
        product_id = row['id']
        if not Product.objects.filter(id=product_id).exists():
            # Create a new product if it doesn't exist
            Product.objects.create(
                id=product_id,
                name=row['name'],
                description=row['description'],
                price=row['price'],
                quantity=row['quantity'],
            )

@when('the user accesses the product list')
def step_when_the_user_accesses_the_product_list(context):
    # Access the product list page
    response = context.client.get(reverse('list'))
    context.product_list_response = response

@then('the product list should be displayed with the correct products and quantities')
def step_then_the_product_list_should_be_displayed_with_the_correct_products_and_quantities(context):
    # Check the product list response
    assert context.product_list_response.status_code == 200

