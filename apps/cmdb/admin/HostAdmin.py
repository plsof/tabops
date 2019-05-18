from django.conf.urls import url
from django.contrib import admin
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin
from django.http import HttpResponseRedirect

from cmdb.models import IDC, Host
from cmdb.tasks import scan_host_job


class HostResource(resources.ModelResource):
    idc = fields.Field(column_name='idc',
        attribute='idc',
        widget=ForeignKeyWidget(IDC, 'name'))

    class Meta:
        model = Host
        fields = ('idc', 'cabinet', 'rack', 'host_name', 'lan_ip',
                  'man_ip', 'kernel', 'kernel_release',
                  'virtual', 'host', 'osrelease', 'saltversion', 'osfinger',
                  'os_family', 'system_serialnumber', 'cpu_model', 'productname', 'osarch',
                  'cpuarch', 'os', 'mem_total', 'num_cpus', 'comments', 'roles')


@admin.register(Host)
class HostAdmin(ImportExportModelAdmin):
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            url(
                r'^scan_host/$',
                self.admin_site.admin_view(self.scan_host),
                name='scan_host',
            ),
        ]
        return custom_urls + urls

    resource_class = HostResource
    change_list_template = 'cmdb_host_list.html'
    change_form_template = 'cmdb_host_form.html'
    list_display = ['idc', 'host_name', 'lan_ip', 'host',
                    'virtual', 'minion_status', 'roles']
    ordering = ['idc', 'host_name']
    search_fields = ['host_name', 'lan_ip', 'roles']
    list_filter = ['idc', 'virtual', 'minion_status']

    def scan_host(self, request):
        scan_host_job('*')
        self.message_user(request, "主机扫描完成")
        return super(HostAdmin, self).changelist_view(request=request)

    def save_formset(self, request, form, formset, change):
        entity = form.save()
        formset.save()

    def response_change(self, request, obj):
        if "_refresh" in request.POST:
            scan_host_job(obj.host_name)
            self.message_user(request, "主机刷新成功")
            return HttpResponseRedirect(".")
        return super().response_change(request, obj)
