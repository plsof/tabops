from django.contrib import admin
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin

from architecture.models import ad
from cmdb.models import IDC
from bstype.models import bussiness_type
from bstype.models import service_type


class adResource(resources.ModelResource):
    idc = fields.Field(column_name='idc',
        attribute='idc',
        widget=ForeignKeyWidget(IDC, 'name'))

    bussiness = fields.Field(column_name='bussiness',
        attribute='bussiness',
        widget=ForeignKeyWidget(bussiness_type, 'name'))

    class Meta:
        model = ad
        fields = ('idc', 'bussiness', 'service', 'ip', 'path', 'port', 'comments', 'update_time')


class serviceFilter(admin.SimpleListFilter):
    title = '服务名称'
    parameter_name = 'service'

    def bussiness_id(self):
        rs = bussiness_type.objects.get(name='ad')
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


@admin.register(ad)
class adAdmin(ImportExportModelAdmin):
    resource_class = adResource
    list_display = ['idc', 'bussiness', 'service', 'ip', 'path', 'port', 'comments']
    ordering = ('idc', 'service', 'ip', 'port')
    search_fields = ['ip']
    list_filter = ['idc', serviceFilter]

