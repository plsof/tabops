from django.db import models

from cmdb.models import ISP, IDCLevel
from common.models import BaseModel


class IDC(BaseModel):
    name = models.CharField(max_length=255, verbose_name='机房名称')
    bandwidth = models.CharField(max_length=255, blank=True, null=True, verbose_name='机房带宽')
    phone = models.CharField(max_length=255, verbose_name='联系电话')
    linkman = models.CharField(max_length=255, null=True, verbose_name='联系人')
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name="机房地址")
    concat_email = models.EmailField(verbose_name='联系邮箱', blank=True, null=True, default="")
    network = models.TextField(blank=True, null=True, verbose_name="IP地址段")
    create_time = models.DateField(auto_now=True, verbose_name='创建时间')
    operator = models.ForeignKey(ISP, on_delete=models.CASCADE, verbose_name='ISP类型')
    type = models.ForeignKey(IDCLevel, on_delete=models.CASCADE, verbose_name='机房类型')
    comment = models.TextField(blank=True, null=True, verbose_name="备注")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "机房"
        verbose_name_plural = verbose_name
