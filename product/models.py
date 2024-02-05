from django.db import models


class ProductCategory(models.Model):
    title = models.CharField(max_length=200, db_index=True, unique=True, verbose_name='عنوان دسته بندی')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='دسته والد',related_name='sub_cat' , null=True, blank=True)
    status = models.BooleanField(verbose_name= 'فعال / غیرفعال', default=True)
    is_delete = models.BooleanField(default=False, verbose_name='حذف شده / نشده')

    class Meta:
        verbose_name = 'دسته بندی محصول'
        verbose_name_plural = 'دسته بندی محصولات'

    def __str__(self):
        return self.title
    
class ProductBrand(models.Model):
    title = models.CharField(max_length=300, db_index=True, unique=True, verbose_name='عنوان برند')
    status = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')
    image = models.ImageField(upload_to='images/brands',blank=True, null=True, verbose_name='تصویر برند')   
    
    class Meta:
        verbose_name =  'برند'
        verbose_name_plural = 'برند ها'
        
    def __str__(self):
        return self.title
        


class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان محصول')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='category', verbose_name='دسته بندی')
    description = models.TextField(verbose_name='توضیحات محصول')
    image = models.ImageField(upload_to='images/products', blank=True, null=True, verbose_name='تصویر محصول')
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, related_name='brand', verbose_name='برند', null=True, blank=True)
    price = models.IntegerField(verbose_name='قیمت')
    status = models.BooleanField(default=True, verbose_name='وضعیت')
    slug = models.SlugField(default="", null=False, blank=True, db_index=True, unique=True, max_length=200,
                            allow_unicode=True, verbose_name='عنوان در url')
    is_delete = models.BooleanField(default=False, verbose_name='حذف شده/ نشده')

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.title


class ProductGallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE , verbose_name="محصول")
    image = models.ImageField(upload_to='images/product_gallery', verbose_name="تصویر")

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = "تصویر گالری"
        verbose_name_plural = "گالری تصاویر"










