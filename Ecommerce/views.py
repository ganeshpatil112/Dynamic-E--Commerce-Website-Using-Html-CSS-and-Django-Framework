from django.shortcuts import render , redirect
from app.models import *
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate_login_logout


def BASE(request):
    return render(request,'base.html'),

def HOME(request):
    sliders = slider.objects.all().order_by('-id')
    banners = banner.objects.all()

    main_category = Main_category.objects.all()
    Product = product.objects.filter(Section__name_=_'Top Deals Of Day')
    print
    
    context = { 'sliders':sliders,
                'banners': banners,
          'main_category': main_category,
                'Product': Product,
    }
    return render(request,'main/home.html',context),

def PRODUCTS_DETAILS(request,slug):
    product = Product.objects.filter(slug_=_slug)
    if product.exists():
        product = product.objects.get(slug=slug)
    else:
        return redirect('404')

    context= { 'product': product,
              }
    return render(request,'product/product_detail.html', context)

def Error404(request):
    return render(request,'Erorrs/404.html')

def REGISTER(request):
    if request.method =='POST':
        username = request.POST.get('uesrname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user =  User{
            username =  username,
            email = email,
        }
        user.set_password(password)
        user.save()
    return redirect('my-account')

def LOGIN(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user  = authenticate(request,username = username , password = password)
        if user is not None:
            login(request_user)
            return redirect('home')
        else:
            return redirect('my_account')
    return render(request,'my-account.html')
    



