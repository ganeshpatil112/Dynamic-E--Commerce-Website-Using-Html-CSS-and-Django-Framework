
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    path('account/login', views.LOGIN , name = 'login'),
    path('account/my-account', views.MY-ACCOUNT , name = 'my-account'),
    path('account/register', views.REGISTER, name = 'register'),
    path('404', views.Error404 , name = '404'),
    path('admin', admin.site.urls),
    path('base', views.BASE , name = 'base'),
    path('', views.HOME , name = 'home')
    path('product/<slug:slug>', views.PRODUCTS_DETAILS, name='product_detail'),


] +static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
