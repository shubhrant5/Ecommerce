"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from customer import views as user_views
from customer.views import OrderView
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='customer/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='customer/logout.html'), name='logout'),
    path('', user_views.home, name='shop-home'),
    path('orders',user_views.OrderView, name='orders'),
    path('cart/checkout',user_views.checkout, name='invoice'),
    path('cart/',user_views.cart, name='cart'),
    path('invoice/',user_views.get_order_details, name='order_details'),
    path('restapi/',user_views.get_data),
    path('restprod/',user_views.ProductList.as_view()),
    path('restprod/<id>',user_views.ProductUpdate.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
