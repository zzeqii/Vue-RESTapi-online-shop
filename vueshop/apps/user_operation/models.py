from datetime import datetime  
  
from django.db import models  
from django.contrib.auth import get_user_model  
  
from goods.models import Goods  
  
# Create your models here.  
User = get_user_model()  
  
  
class UserFav(models.Model):  
    """ 
    saving item 
    """  
    user = models.ForeignKey(User, verbose_name="user",on_delete=models.CASCADE)  
    goods = models.ForeignKey(Goods, verbose_name="item", help_text="item id",on_delete=models.CASCADE)  
    add_time = models.DateTimeField(default=datetime.now, verbose_name="adding time")  
  
    class Meta:  
        verbose_name = 'saves'  
        verbose_name_plural = verbose_name  
        unique_together = ("user", "goods")  
  
    def __str__(self):  
        return self.user.username  
  
  
class UserLeavingMessage(models.Model):  
    """ 
    review 
    """  
    MESSAGE_CHOICES = (  
        (1, "comment"),  
        (2, "feedback"),  
        (3, "query"),  
        (4, "after sales"),  
        (5, "watching for buying")  
    )  
    user = models.ForeignKey(User, verbose_name="user",on_delete=models.CASCADE)  
    message_type = models.IntegerField(default=1, choices=MESSAGE_CHOICES, verbose_name="comment type",  
                                       help_text="comment type: 1(comment),2(feedback),3(query),4(after sales),5(watchong for buying)")  
    subject = models.CharField(max_length=100, default="", verbose_name="topic")  
    message = models.TextField(default="", verbose_name="comment content", help_text="comment content")  
    file = models.FileField(upload_to="message/images/", verbose_name="uploads", help_text="uploads")  
    add_time = models.DateTimeField(default=datetime.now, verbose_name="adding time")  
  
    class Meta:  
        verbose_name = "comment"  
        verbose_name_plural = verbose_name  
  
    def __str__(self):  
        return self.subject  
  
  
class UserAddress(models.Model):  
    """ 
    address 
    """  
    user = models.ForeignKey(User, verbose_name="user",on_delete=models.CASCADE)  
    province = models.CharField(max_length=100, default="", verbose_name="state")  
    city = models.CharField(max_length=100, default="", verbose_name="city")  
    district = models.CharField(max_length=100, default="", verbose_name="area")  
    address = models.CharField(max_length=100, default="", verbose_name="address")  
    signer_name = models.CharField(max_length=100, default="", verbose_name="receiver")  
    signer_mobile = models.CharField(max_length=11, default="", verbose_name="phone")  
    add_time = models.DateTimeField(default=datetime.now, verbose_name="adding time")  
  
    class Meta:  
        verbose_name = "address"  
        verbose_name_plural = verbose_name  
  
    def __str__(self):  
        return self.address