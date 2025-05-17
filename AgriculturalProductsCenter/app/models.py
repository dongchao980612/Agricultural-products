from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    origin = models.CharField(max_length=100, verbose_name='产地')
    description = models.TextField("商品描述")
    image = models.ImageField("商品图片", upload_to='products/')
    stock = models.PositiveIntegerField("库存", default=0)
    xiaoliang = models.IntegerField(default=0, verbose_name='销量')
    is_active = models.BooleanField("上架状态", default=True)

    def __str__(self):
        return self.name

# 用户资料模型
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=20, blank=True, default='')
    address = models.TextField(blank=True, default='')
    user_type = models.PositiveSmallIntegerField(
        choices=((1, '普通用户'), (2, '管理员')),
        default=1
    )

    def __str__(self):
        return self.user.username+"的资料"