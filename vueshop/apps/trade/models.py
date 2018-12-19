from datetime import datetime  
  
from django.db import models  
from django.contrib.auth import get_user_model  
  
from goods.models import Goods  
  
User = get_user_model()  
  
  
# Create your models here.  
  
  
class ShoppingCart(models.Model):  
    """ 
    shopping cart 
    """  
    user = models.ForeignKey(User, verbose_name="user",on_delete=models.CASCADE)  
    goods = models.ForeignKey(Goods, verbose_name="item",on_delete=models.CASCADE)  
    nums = models.IntegerField(default=0, verbose_name="order")  
  
    add_time = models.DateTimeField(default=datetime.now, verbose_name="adding time")  
  
    class Meta:  
        verbose_name = 'Shopping Cart'  
        verbose_name_plural = verbose_name  
        unique_together = ("user", "goods")  
  
    def __str__(self):  
        return "%s(%d)".format(self.goods.name, self.nums)  
  
  
class OrderInfo(models.Model):  
    """ 
    order infromation 
    """  
    ORDER_STATUS = (  
        ("TRADE_SUCCESS", "Success"),  
        ("TRADE_CLOSED", "Overtime"),  
        ("WAIT_BUYER_PAY", "Creating order"),  
        ("TRADE_FINISHED", "transnction finished"),  
        ("paying", "waiting for paying"),  
    )  
  
    user = models.ForeignKey(User, verbose_name="user",on_delete=models.CASCADE)  
    order_sn = models.CharField(max_length=30, null=True, blank=True, unique=True, verbose_name="order number")  
    trade_no = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name=u"transaction number")  
    pay_status = models.CharField(choices=ORDER_STATUS, default="paying", max_length=30, verbose_name="status")  
    post_script = models.CharField(max_length=200, verbose_name="comment")  
    order_mount = models.FloatField(default=0.0, verbose_name="price")  
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name="payment time")  
  
    # 用户信息  
    address = models.CharField(max_length=100, default="", verbose_name="address")  
    signer_name = models.CharField(max_length=20, default="", verbose_name="receiver")  
    singer_mobile = models.CharField(max_length=11, verbose_name="phone")  
  
    add_time = models.DateTimeField(default=datetime.now, verbose_name="adding time")  
  
    class Meta:  
        verbose_name = "order"  
        verbose_name_plural = verbose_name  
  
    def __str__(self):  
        return str(self.order_sn)  
  
  
class OrderGoods(models.Model):  
    """ 
    details of the orders 
    """  
    order = models.ForeignKey(OrderInfo, verbose_name="order info", related_name="goods",on_delete=models.CASCADE)  
    goods = models.ForeignKey(Goods, verbose_name="item",on_delete=models.CASCADE)  
    goods_num = models.IntegerField(default=0, verbose_name="item number")  
  
    add_time = models.DateTimeField(default=datetime.now, verbose_name="adding time")  
  
    class Meta:  
        verbose_name = "order item"  
        verbose_name_plural = verbose_name  
  
    def __str__(self):  
        return str(self.order.order_sn)  
