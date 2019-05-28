from django.db import models

from common.models import BaseModel
from common.constants import SWARM_ROLE
from cmdb.models import IDC


class Vas(BaseModel):
    idc = models.ForeignKey(IDC, on_delete=models.CASCADE, verbose_name='机房', blank=True, null=True)
    role = models.IntegerField(verbose_name='node角色', default=0, choices=SWARM_ROLE)
    node = models.GenericIPAddressField(protocol='IPv4', blank=True, null=True, verbose_name="node地址")
    mode = models.CharField(max_length=255, verbose_name='模式')
    comments = models.TextField(max_length=255, blank=True, null=True, verbose_name="备注")

    # def __str__(self):
    #     return self.node

    class Meta:
        verbose_name = "601四川移动"
        verbose_name_plural = verbose_name
