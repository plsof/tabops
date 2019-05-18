from django.contrib import admin
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin

from cmdb.models import IDC
from cmdb.models import SHost
from cmdb.models import Host


class HostInline(admin.TabularInline):
    model = Host
    fields = ['lan_ip']
    verbose_name = "VM"
    verbose_name_plural = "VM"
    extra = 0


class SHostResource(resources.ModelResource):
    idc = fields.Field(column_name='idc',
        attribute='idc',
        widget=ForeignKeyWidget(IDC, 'name'))

    class Meta:
        model = Host
        fields = ('idc', 'cabinet', 'rack', 'name', 'lan_ip', 'man_ip',
                  'system_serialnumber', 'os', 'mem_total', 'num_cpus', 'volume')


@admin.register(SHost)
class SHostAdmin(ImportExportModelAdmin):
    resource_class = SHostResource
    list_display = ['idc', 'cabinet', 'rack', 'name', 'lan_ip',
                    'system_serialnumber', 'update_time']
    ordering = ['idc', 'cabinet', 'rack', 'name']
    search_fields = ['name']
    list_filter = ['idc', 'cabinet', 'rack']
    inlines = [HostInline]

