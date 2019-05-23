from django.db import models

from bstype.models import bussiness_type
from common.models import BaseModel


class service_type(BaseModel):
    bussiness = models.ForeignKey(bussiness_type, on_delete=models.CASCADE, verbose_name='业务类型')
    name = models.CharField(max_length=255, unique=True, verbose_name='服务类型')
    comments = models.TextField(blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '服务类型'
        verbose_name_plural = verbose_name
