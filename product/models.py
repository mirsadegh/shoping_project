from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان محصول')
    description = models.TextField(verbose_name='توضیحات محصول')
    image = models.ImageField(upload_to='images/products', blank=True, null=True, verbose_name='تصویر محصول')
    price = models.IntegerField(verbose_name='قیمت')
    status = models.BooleanField(default=True, verbose_name='وضعیت')
    slug = models.SlugField(default="", null=False, blank=True, db_index=True, unique=True, max_length=200  ,verbose_name='عنوان در url')
    is_delete = models.BooleanField(verbose_name='حذف شده/ نشده')

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


    def __str__(self):
        return self.title



class ProductGallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE , verbose_name="محصول")
    image =   models.ImageField(upload_to='images/product_gallery', verbose_name="تصویر")


    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = "تصویر گالری"
        verbose_name_plural = "گالری تصاویر"










