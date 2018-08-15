from django.db import models

# Create your models here.
class Commodity(models.Model):
    goods_name = models.CharField(
        max_length=30,
        verbose_name="商品名称"
    )
    goods_price = models.IntegerField(
        verbose_name="商品价格"
    )
    create_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="生产日期"
    )
    def __str__(self):
        return self.name+str(self.goods_pirce)
    class Meta:
        verbose_name = "商品类",
        db_table = "商品列表"