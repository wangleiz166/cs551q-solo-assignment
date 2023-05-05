from django.shortcuts import render
from order.models import Order
from product_csv.models import Product
from user.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import plotly.graph_objs as go
from plotly.offline import plot


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
    paginator = Paginator(order_list, 10)  # 每页显示10个商品
    page = request.GET.get('page') or 1  # 如果请求的页码未设置或为空字符串，设置为1


    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        # 如果请求的页码不是整数，则显示第一页
        orders = paginator.page(1)
    except EmptyPage:
        # 如果请求的页码超出范围，则显示最后一页
        orders = paginator.page(paginator.num_pages)

    
    return render(request, 'admin_list.html',{'orders':orders})



def userList(request):
    if not is_admin(request):
        return render(request, 'not_admin.html')
    user_list = User.objects.all().order_by('id')
    # Pagination    
    paginator = Paginator(user_list, 10)  # 每页显示10个商品
    page = request.GET.get('page') or 1  # 如果请求的页码未设置或为空字符串，设置为1


    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        # 如果请求的页码不是整数，则显示第一页
        users = paginator.page(1)
    except EmptyPage:
        # 如果请求的页码超出范围，则显示最后一页
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

