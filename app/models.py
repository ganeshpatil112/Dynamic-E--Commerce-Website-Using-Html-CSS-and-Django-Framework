from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse




# Create your models here.
class slider(models.Model):
    DISCOUNT_DEAL = (
      ('HOT DEAL','HOT DEAL'),
      ('New Arraivels','New Arraivels'),
    )

    Image = models.ImageField(upload_to='media/slider_imgs')
    Discount_Deals = models.CharField(choices=DISCOUNT_DEAL,max_length=100)
    SALE = models.IntegerField()
    Brand_Name = models.CharField(max_length=100)
    Discount = models.IntegerField()
    Link = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.Brand_Name

class banner(models.Model):
    
    Quote = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='media/banner_imgs')
    Discount_Deals = models.CharField(max_length=100)
    Discount = models.IntegerField() 



    def __str__(self):
        return self.Quote
    
class Main_category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    Main_category = models.ForeignKey(Main_category, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name + " -- " + self.Main_category.name  
           
class Sub_category(models.Model):
    Category = models.ForeignKey(Category, on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.Category.Main_category.name + " -- " + self.Category.name + " -- " + self.name
    
class Section(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class product(models.Model):
    total_quantity = models.IntegerField()
    Availability = models.IntegerField()
    featured_image = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    Discount = models.IntegerField()
    Product_information = RichTextField(null=True)
    model_Name = models.CharField(max_length=100)
    categories = models.ForeignKey(Category, on_delete = models.CASCADE)
    Tags = models.CharField(max_length=100)
    Description = RichTextField()
    section = models.ForeignKey(Section, on_delete=models.DO_NOTHING)
    slug = models.SlugField(default='', max_length=500, null=True, blank=True)

    def __str__(self):
        return self.product_name
    
    def get_absolute_url(self):
    	return reverse("product_detail", kwargs={'slug': self.slug})

    class Meta:
    	db_table = "app_Product"

def create_slug(instance, new_slug=None):
	slug = slugify(instance.product_name)
	if new_slug is not None:
       slug = new_slug
	qs = Product.objects.filter(slug=slug).order_by('-id')
	exists = qs.exists()
	if exists:
    	new_slug = "%s-%s" % (slug, qs.first().id)
    	return create_slug(instance, new_slug=new_slug)
	return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
       instance.slug = create_slug(instance)
pre_save.connect(pre_save_post_receiver, Product)

class Product_Image(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    Image_url = models.CharField(max_length=100)

class Additional_Information(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    specification = models.CharField(max_length=100)
    detail = models.CharField(max_length=100)

def LOGIN(request):
     if request.method == 'POST':
          username = request.POST.get
     return render(request,'account/my-account.html')






