from django.shortcuts import render, redirect
from order.models import Cart, Order
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def cart(request):
    user_id = request.COOKIES.get('userid', None)
    if not user_id:
        return redirect('/user/login')
    cart_items = Cart.objects.all()
    total_price = sum([float(item.product_price.replace("₹", "").replace(",", "")) * item.product_quantity for item in cart_items])
    context = {'cart_items': cart_items, 'total_price': total_price}
    return render(request, 'cart.html', context)

def order(request):
    user_id = request.COOKIES.get('userid', None)
    if not user_id:
        return redirect('/user/login')
    
    orders = Order.objects.filter(user_id=user_id)

    for order in orders:
        price = float(order.product_price.replace("₹", ""))
        quantity = order.product_quantity
        total_price = price * quantity
        order.total_price = f"₹{total_price}"

    return render(request, 'order.html', {'orders': orders})

def add_to_cart(request):
    if request.method == 'POST':
        # Get form data
        user_id = request.COOKIES.get('userid', None)
        if not user_id:
           return redirect('/user/login')
        product_id = request.POST.get('product_id')
        product_name = request.POST.get('product_name')
        product_price = request.POST.get('product_price')
        product_quantity = int(request.POST.get('product_quantity'))

        # Check if the item already exists in the shopping cart
        try:
            cart_item = Cart.objects.get(user_id=user_id, product_id=product_id)
            # Update the number of items if present
            cart_item.product_quantity += product_quantity
            cart_item.save()
        except ObjectDoesNotExist:
            # If not present, add new cart item
            cart_item = Cart(user_id=user_id, product_id=product_id, product_name=product_name, product_price=product_price, product_quantity=product_quantity)
            cart_item.save()

        # Jump to shopping cart page
        return redirect('/order/cart')
    

def remove_cart(request, id):
    # Delete items from the shopping cart
    cart_item = Cart.objects.get(id=id)
    cart_item.delete()

    # Display success message to user and redirect to shopping cart page
    return redirect('/order/cart')


def checkout(request):
    user_id = request.COOKIES.get('userid', None) 

    # Get all items in the cart for the current user
    cart_items = Cart.objects.filter(user_id=user_id)

    if cart_items:
        # Add items from the shopping cart to the Order model
        for item in cart_items:
            order = Order(
                user_id=user_id,
                product_id=item.product_id,
                product_name=item.product_name,
                product_price=item.product_price,
                product_quantity=item.product_quantity,
            )
            order.save()

        # Delete items from the shopping cart
        cart_items.delete()

        # Display success message to user and redirect to confirmation page
        return redirect('/order') 
    else:
        return redirect('/order/cart')