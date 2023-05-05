from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from product_csv.models import Product,Review
from django.db.models import Q,Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import sqlite3

# Create your views here.
def index(request):
    products = Product.objects.all()[:4]
    hotproducts = Product.objects.filter(
        Q(category="Home&Kitchen|Kitchen&HomeAppliances|SmallKitchenAppliances|MixerGrinders")
    )[:6]
    mou_products = Product.objects.filter(
        Q(category="Electronics|WearableTechnology|SmartWatches")
    )[:4]
    el_products = Product.objects.filter(
        Q(category="Electronics|Mobiles&Accessories|Smartphones&BasicMobiles|Smartphones")
    )[:4]
    cook_products = Product.objects.filter(
        Q(category="Home&Kitchen|Heating,Cooling&AirQuality|RoomHeaters|FanHeaters")
    )[:4]
    context = {
        'products': products,
        'mou_products': mou_products,
        'el_products': el_products,
        'cook_products': cook_products, 
        'hotproducts': hotproducts
    }
    return render(request, 'index.html', context)

def list(request):
    products_list = Product.objects.all().order_by('id')

    # Get product count by category
    categories = (
        products_list.values("category")
        .annotate(count=Count("id"))
        .order_by("category")
    )

    # Search
    search_query = request.GET.get('search_query')
    search_field = 'name'
    if search_query:
        products_list = products_list.filter(**{f"{search_field}__icontains": search_query})

    # Filter by category
    category_query = request.GET.get('category')
    if category_query:
        products_list = products_list.filter(category=category_query)
        
    # Pagination    
    paginator = Paginator(products_list, 8)  # 每页显示8个商品
    page = request.GET.get('page') or 1  # 如果请求的页码未设置或为空字符串，设置为1
    
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # 如果请求的页码不是整数，则显示第一页
        products = paginator.page(1)
    except EmptyPage:
        # 如果请求的页码超出范围，则显示最后一页
        products = paginator.page(paginator.num_pages)

    context = {
        'products': products,
        'categories': categories,
        'search_query': search_query,
        'category_query': category_query,
    }

    return render(request, 'list.html', context=context)



def detail(request, id):
    products = Product.objects.filter(product_id=id)
    detail = None
    if products.exists():
        detail = products.first()
        reviewList = Review.objects.filter(product_id=id)
        review_count = len(reviewList)
        hotproducts = Product.objects.filter(
            Q(category=detail.category) & ~Q(product_id=id)
        )[:4]
        return render(request, 'detail.html', {'detail': detail, 'review': reviewList, 'review_count':review_count, 'hotproducts':hotproducts})
    else:
        return HttpResponseNotFound('Product not found')
