from django.db import models
from smart_selects.db_fields import ChainedForeignKey

from cmdb.models import Cabinet, IDC
from common.models import BaseModel


class Rack(BaseModel):
    idc = models.ForeignKey(IDC, verbose_name='IDC', on_delete=models.CASCADE, blank=True, null=True)
    cabinet = ChainedForeignKey(
        Cabinet,
        verbose_name="机柜",
        chained_field="idc",
        chained_model_field="idc",
        show_all=False,
        auto_choose=True,
        sort=True, blank=True, null=True
    )
    name = models.CharField(max_length=30, verbose_name="机架名称")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "机架"
        verbose_name_plural = verbose_name
        unique_together = (('idc', 'cabinet', 'name'),)
