from django.db import models

# Create your models here.
from DjangoUeditor.models import UEditorField 
from datetime import datetime  
from django.db import models  
  
  
class GoodsCategory(models.Model):  
    """ 
    category
    """  
    CATEGORY_TYPE = (  
        (1, "firs category"),  
        (2, "second category"),  
        (3, "third category"),  
    )  
  
    name = models.CharField(default="", max_length=30, verbose_name="category name", help_text="category name")  
    code = models.CharField(default="", max_length=30, verbose_name="category code", help_text="category code")  
    desc = models.TextField(default="", verbose_name="description", help_text="description")  
    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="category level", help_text="category level")  
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="parent category", help_text="parent category",  
                                        related_name="sub_cat",on_delete=models.CASCADE
                                        )  
    is_tab = models.BooleanField(default=False, verbose_name="nevigation or not", help_text="nevigation or not")  
    add_time = models.DateTimeField(default=datetime.now, verbose_name="adding time")  
  
    class Meta:  
        verbose_name = "category"  
        verbose_name_plural = verbose_name  
  
    def __str__(self):  
        return self.name  
  
  
class GoodsCategoryBrand(models.Model):  
    """ 
    brand 
    """  
    category = models.ForeignKey(GoodsCategory, related_name='brands', null=True, blank=True, verbose_name="category",on_delete=models.CASCADE)  
    name = models.CharField(default="", max_length=30, verbose_name="brand", help_text="brand")  
    desc = models.TextField(default="", max_length=200, verbose_name="brand description", help_text="brand description")  
    image = models.ImageField(max_length=200, upload_to="brands/")  
    add_time = models.DateTimeField(default=datetime.now, verbose_name="adding time")  
  
    class Meta:  
        verbose_name = "brands"  
        verbose_name_plural = verbose_name  
        db_table = "goods_goodsbrand"  
  
    def __str__(self):  
        return self.name  
  
  
class Goods(models.Model):  
    """ 
    goods 
    """  
    category = models.ForeignKey(GoodsCategory, verbose_name="brands",on_delete=models.CASCADE)  
    goods_sn = models.CharField(max_length=50, default="", verbose_name="unique no.")  
    name = models.CharField(max_length=100, verbose_name="name")  
    click_num = models.IntegerField(default=0, verbose_name="views")  
    sold_num = models.IntegerField(default=0, verbose_name="sales")  
    fav_num = models.IntegerField(default=0, verbose_name="saves")  
    goods_num = models.IntegerField(default=0, verbose_name="stocks")  
    market_price = models.FloatField(default=0, verbose_name="market price")  
    shop_price = models.FloatField(default=0, verbose_name="shop price")  
    goods_brief = models.TextField(max_length=500, verbose_name="short description")  
    goods_desc = UEditorField(verbose_name="content", imagePath="goods/images/", width=1000, height=300,  
                               filePath="goods/files/", default='')  
    ship_free = models.BooleanField(default=True, verbose_name="freight")  
    goods_front_image = models.ImageField(upload_to="goods/images/", null=True, blank=True, verbose_name="cover page")  
    is_new = models.BooleanField(default=False, verbose_name="new")  
    is_hot = models.BooleanField(default=False, verbose_name="popular")  
    add_time = models.DateTimeField(default=datetime.now, verbose_name="adding time")  
  
    class Meta:  
        verbose_name = 'item'  
        verbose_name_plural = verbose_name  
  
    def __str__(self):  
        return self.name  
  
  
class IndexAd(models.Model):  
    category = models.ForeignKey(GoodsCategory, related_name='category', verbose_name="category",on_delete=models.CASCADE)  
    goods = models.ForeignKey(Goods, related_name='goods',on_delete=models.CASCADE)  
  
    class Meta:  
        verbose_name = 'advertisement'  
        verbose_name_plural = verbose_name  
  
    def __str__(self):  
        return self.goods.name  
  
  
class GoodsImage(models.Model):  
    """ 
    banner
    """  
    goods = models.ForeignKey(Goods, verbose_name="item", related_name="images",on_delete=models.CASCADE)  
    image = models.ImageField(upload_to="", verbose_name="photo", null=True, blank=True)  
    add_time = models.DateTimeField(default=datetime.now, verbose_name="adding time")  
  
    class Meta:  
        verbose_name = 'photo'  
        verbose_name_plural = verbose_name  
  
    def __str__(self):  
        return self.goods.name  
  
  
class Banner(models.Model):  
    """ 
    banner item 
    """  
    goods = models.ForeignKey(Goods, verbose_name="item",on_delete=models.CASCADE)  
    image = models.ImageField(upload_to='banner', verbose_name="pic")  
    index = models.IntegerField(default=0, verbose_name="order")  
    add_time = models.DateTimeField(default=datetime.now, verbose_name="adding time")  
  
    class Meta:  
        verbose_name = 'banner item'  
        verbose_name_plural = verbose_name  
  
    def __str__(self):  
        return self.goods.name  
  
  
class HotSearchWords(models.Model):  
    """ 
    popular word 
    """  
    keywords = models.CharField(default="", max_length=20, verbose_name="popular word")  
    index = models.IntegerField(default=0, verbose_name="sorting")  
    add_time = models.DateTimeField(default=datetime.now, verbose_name="adding time")  
  
    class Meta:  
        verbose_name = 'popular word'  
        verbose_name_plural = verbose_name  
  
    def __str__(self):  
        return self.keywords  
