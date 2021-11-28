from django.db import models

from django.urls import reverse

from category.models import Category

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(
        max_length=200, unique=True, verbose_name="نام محصول")
    slug = models.SlugField(max_length=250, unique=True)
    descriptions = models.TextField(
        max_length=500, blank=True, verbose_name="توضیحات")
    price = models.IntegerField(verbose_name="قیمت")
    images = models.ImageField(
        upload_to="photos/products", blank=True, verbose_name="تصویر")
    stock = models.IntegerField(verbose_name="موجودی")
    is_available = models.BooleanField(default=True,  verbose_name="وضعیت")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="دسته")
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name="تاریخ ثبت")
    modified_date = models.DateTimeField(
        auto_now=True, verbose_name="تاریخ ویرایش")

    class Meta:
        verbose_name = 'محصولات'
        verbose_name_plural = 'محصولات'

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name


class VaridationManager(models.Manager):
    
    def colors(self):
        return super(VaridationManager,self).filter(variation_category='color', is_active=True)
    
    def sizes(self):
        return super(VaridationManager,self).filter(variation_category='size', is_active=True)


variation_category_choice=(
    ('color','color'),
    ('size','size'),
)

class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    variation_category = models.CharField(max_length=100, choices=variation_category_choice, verbose_name='دسته بندی')
    variation_value = models.CharField(max_length=100)
    variation_name = models.CharField(max_length=100,null=True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")
    
    objects = VaridationManager()

    class Meta:
        verbose_name = 'مشخصات'
        verbose_name_plural = 'مشخصات'
    
    def __str__(self):
        return self.variation_value
        