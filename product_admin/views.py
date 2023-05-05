from django.shortcuts import render,redirect
from order.models import Order
from product_csv.models import Product
from user.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import plotly.graph_objs as go
from plotly.offline import plot


def set_general(request, user_id):
    if not is_admin(request):
        return render(request, 'not_admin.html')

    user = User.objects.get(id=user_id)
    user.is_admin = False
    user.save()

    return redirect('userList')

def set_admin(request, user_id):
    if not is_admin(request):
        return render(request, 'not_admin.html')

    user = User.objects.get(id=user_id)
    user.is_admin = True
    user.save()

    return redirect('userList')

def is_admin(request):
    user_id = request.COOKIES.get('userid', None)
    
    if user_id:
        try:
            user = User.objects.get(id=user_id)
            if user.is_admin:
                return True
        except User.DoesNotExist:
            pass

    return False

def list(request):
    if not is_admin(request):
        return render(request, 'not_admin.html')
    
    order_list = Order.objects.all().order_by('id')
    # Pagination    
    paginator = Paginator(order_list, 10)  
    page = request.GET.get('page') or 1 


    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        # If the requested page number is not an integer, then the first page is displayed
        orders = paginator.page(1)
    except EmptyPage:
        # If the requested page number is out of range, the last page will be displayed
        orders = paginator.page(paginator.num_pages)

    
    return render(request, 'admin_list.html',{'orders':orders})



def userList(request):
    if not is_admin(request):
        return render(request, 'not_admin.html')
    user_list = User.objects.all().order_by('id')
    # Pagination    
    paginator = Paginator(user_list, 10)  # 10 items per page
    page = request.GET.get('page') or 1  # If the requested page number is not set or is an empty string, set to 1


    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    
    return render(request, 'user_list.html',{'users':users})


def dashboard(request):
    if not is_admin(request):
        return render(request, 'not_admin.html')
    orders = Order.objects.all().order_by('order_date')
    data = [
        go.Scatter(
            x=[order.order_date for order in orders],
            y=[order.product_quantity for order in orders],
            name='Quantity',
            mode='lines'
        ),
        go.Scatter(
            x=[order.order_date for order in orders],
            y=[order.product_price for order in orders],
            name='Price',
            mode='lines'
        )
    ]
    layout = go.Layout(
        title='Sales Over Time',
        xaxis=dict(title='Date'),
        yaxis=dict(title='Sales')
    )
    chart = plot(go.Figure(data=data, layout=layout), output_type='div')

    products = Product.objects.all()
    prices = [float(product.price.replace('₹', '').replace(',', '')) for product in products]

    data = [go.Histogram(x=prices)]
    layout = go.Layout(
    title='Product Prices Distribution',
    xaxis=dict(title='Price', range=[0, 10000]),
    yaxis=dict(title='Count')
)
    chart2 = plot(go.Figure(data=data, layout=layout), output_type='div')

    return render(request, 'dashboard.html', {'chart': chart,'chart2':chart2})

