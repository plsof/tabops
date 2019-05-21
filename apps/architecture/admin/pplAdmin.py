from django.contrib import admin
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin

from architecture.models import ppl
from cmdb.models import IDC
from bstype.models import bussiness_type
from bstype.models import service_type


class pplResource(resources.ModelResource):
    idc = fields.Field(column_name='idc',
        attribute='idc',
        widget=ForeignKeyWidget(IDC, 'name'))

    bussiness = fields.Field(column_name='bussiness',
        attribute='bussiness',
        widget=ForeignKeyWidget(bussiness_type, 'name'))

    # 导入时不能区分出对应那个service，暂时service不导入（readonly） 待解决。。。
    service = fields.Field(column_name='service',
        attribute='service',
        widget=ForeignKeyWidget(service_type, 'name'),
        readonly=True)

    class Meta:
        model = ppl


class serviceFilter(admin.SimpleListFilter):
    title = '服务名称'
    parameter_name = 'service'

    def bussiness_id(self):
        rs = bussiness_type.objects.get(name='ppl')
        return rs.id

    def lookups(self, request, model_admin):
        rs = set([c for c in service_type.objects.filter(bussiness=self.bussiness_id())])
        v = set()
        for obj in rs:
            if obj is not None:
                v.add((obj.id, obj.name))
        return v

    def queryset(self, request, queryset):
        if 'service' in request.GET:
            service = request.GET['service']
            return queryset.filter(service=service)
        else:
            return queryset.all()


@admin.register(ppl)
class pplAdmin(ImportExportModelAdmin):
    resource_class = pplResource
    list_display = ['idc', 'bussiness', 'service', 'ip', 'path', 'port', 'update_time']
    ordering = ('idc', 'service', 'ip', 'port')
    search_fields = ['ip']
    list_filter = ['idc', serviceFilter]
