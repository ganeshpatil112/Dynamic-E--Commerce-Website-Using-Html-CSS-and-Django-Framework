from django.contrib import admin
from .models import *

class Product_Images(admin.TabularInline):
    model = Product_Image

class Additional_Information(admin.TabularInline):
    model = Additional_Information

class Product_Admin(admin.ModelAdmin):
    inlines = (Product_Images,Additional_Information)
    list_display = ('product_name','price','categories','section')
    list_editable = ('categories','section')

# Register your models here.
admin.site.register(Section)
admin.site.register(product)
admin.site.register(Product_Image)
admin.site.register(Additional_Information)
admin.site.register(slider)
admin.site.register(banner)
admin.site.register(Main_category)
admin.site.register(Sub_category)
admin.site.register(Category)


