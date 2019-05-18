from django.db import models
from smart_selects.db_fields import ChainedForeignKey

from cmdb.models import IDC, Cabinet, Rack
from common.models import BaseModel


class SHost(BaseModel):
    idc = models.ForeignKey(IDC, on_delete=models.CASCADE, verbose_name='机房', blank=True, null=True)
    cabinet = ChainedForeignKey(
        Cabinet,
        verbose_name="机柜",
        chained_field="idc",
        chained_model_field="idc",
        show_all=False,
        auto_choose=True,
        sort=True, blank=True, null=True
    )
    rack = ChainedForeignKey(
        Rack,
        verbose_name="机架",
        chained_field="cabinet",
        chained_model_field="cabinet",
        show_all=False,
        auto_choose=True,
        sort=True, blank=True, null=True
    )
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name="主机名")
    lan_ip = models.GenericIPAddressField(protocol='IPv4', blank=True, null=True, verbose_name="内网IP地址")
    man_ip = models.GenericIPAddressField(protocol='IPv4', blank=True, null=True, verbose_name="管理IP地址")
    system_serialnumber = models.CharField(max_length=255, blank=True, null=True, verbose_name="SN号")
    os = models.CharField(max_length=255, blank=True, null=True, verbose_name="操作系统")
    mem_total = models.IntegerField(blank=True, null=True, verbose_name="内存大小")
    num_cpus = models.IntegerField(blank=True, null=True, verbose_name="CPU数量")
    volume = models.CharField(max_length=255, blank=True, null=True, verbose_name="磁盘容量")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "宿主机"
        verbose_name_plural = verbose_name
