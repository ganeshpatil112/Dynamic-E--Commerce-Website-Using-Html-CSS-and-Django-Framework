from django.shortcuts import render , redirect
from app.models import *

def BASE(request):
    return render(request,'base.html'),

def HOME(request):
    sliders = slider.objects.all().order_by('-id')
    banners = banner.objects.all()
    main_category = Main_category.objects.all()
    
    context = { 'sliders':sliders,
                'banners': banners,
          'main_category': main_category,
    }
    return render(request,'main/home.html',context)



