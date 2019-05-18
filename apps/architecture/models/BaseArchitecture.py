from django.db import models
from smart_selects.db_fields import ChainedForeignKey

from cmdb.models import IDC
from bstype.models import bussiness_type, service_type
from common.models import BaseModel


class BaseArchitecture(BaseModel):
    idc = models.ForeignKey(IDC, on_delete=models.CASCADE, verbose_name='机房', blank=True, null=True)
    bussiness = models.ForeignKey(bussiness_type, on_delete=models.CASCADE, verbose_name='业务名称', blank=True, null=True)
    service = ChainedForeignKey(
        service_type,
        verbose_name="服务名称",
        chained_field="bussiness",
        chained_model_field="bussiness",
        show_all=False,
        auto_choose=True,
        sort=True, blank=True, null=True
    )
    ip = models.GenericIPAddressField(protocol='IPv4', blank=True, null=True, verbose_name="IP地址")
    path = models.CharField(max_length=255, blank=True, null=True, verbose_name='部署路径')
    port = models.IntegerField(blank=True, null=True, verbose_name="端口号")
    comments = models.TextField(max_length=255, blank=True, null=True, verbose_name="备注")

    # def __str__(self):
    #     return self.service

    class Meta:
        abstract = True

