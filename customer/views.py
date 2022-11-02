from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .models import Category, Products, Order, Cart, Order_List


@login_required
def OrderView(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        print(order_id)

    customer = request.user
    orders = Order.get_orders_by_customer(customer.id)
    return render(request , 'customer/orders.html'  , {'orders' : orders})


def get_order_details(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        order_list= Order_List.get_order_list_by_id(order_id)
        for order in order_list:
            print(order)
        return render(request , 'customer/order_details.html', {'order_list':order_list})

@login_required
def checkout(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.user
        products = Cart.get_cart_by_customer(customer.id)
        total_price =0
        for product in products:
            price = product.quantity * product.product.price
            total_price =total_price + price
        order_data= Order(customer=customer,price=total_price,address=address,phone=phone)
        order_data.save()
        for product in products:
            print(product)
            order_product=Order_List(order=order_data,product=product.product,quantity=product.quantity)
            order_product.save()

        dataset={
            'address' : address,
            'phone'   : phone,
            'customer': customer,
            'products': products,
            'total_price':total_price}
        return render(request, 'customer/invoice.html',dataset)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'customer/register.html', {'form': form})


@login_required
def cart(request):
    if 'tick' in request.POST:
        product =Cart.get_products_from_cart(request.POST.get('product'))
        new_quantity = request.POST.get('quantity')
        if product:
            product.update(quantity=new_quantity)
            return redirect('cart')
    if 'delete' in request.POST:
        product =Cart.get_products_from_cart(request.POST.get('product'))
        product.delete()
        return redirect('cart')
    customer = request.user
    products = Cart.get_cart_by_customer(customer.id)
    return render(request , 'customer/cart.html'  , {'products' : products})

def add_to_cart(request):
    print(request.user)
    product=request.POST.get('product')
    print(product)

    return render(request, 'customer/home.html')


def home(request):
    if request.method == 'POST':
        product =Products.get_products_by_id(request.POST.get('product'))
        product_in_cart =Cart.get_products_from_cart(request.POST.get('product'))

        if product_in_cart:
            new_quantity = product_in_cart[0].quantity + 1
            product_in_cart.update(quantity=new_quantity)
            return HttpResponseRedirect('/')
        else:
            customer=request.user
            cart_data=Cart(product=product[0],customer=customer,quantity=1)
            cart_data.save()
            return HttpResponseRedirect('/')

    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Products.get_all_products_by_categoryid(categoryID)
    else:
        products = Products.get_all_products()

    context = {
        'posts': categories,
        'products': products
    }
    return render(request, 'customer/home.html',context)
