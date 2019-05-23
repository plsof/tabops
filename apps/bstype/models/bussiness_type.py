from django.db import models

from common.models import BaseModel
from common.constants import BS_TYPE


class bussiness_type(BaseModel):
    name = models.CharField(max_length=255, unique=True, verbose_name='业务名称')
    bs_type = models.IntegerField(verbose_name='业务类型', default=0, choices=BS_TYPE)
    comments = models.TextField(blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '业务类型'
        verbose_name_plural = verbose_name
