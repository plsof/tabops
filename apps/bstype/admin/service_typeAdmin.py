from django.contrib import admin
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin

from bstype.models import bussiness_type
from bstype.models import service_type


class serviceResource(resources.ModelResource):
    bussiness = fields.Field(column_name='bussiness',
        attribute='bussiness',
        widget=ForeignKeyWidget(bussiness_type, 'name'))

    class Meta:
        model = service_type


@admin.register(service_type)
class serviceAdmin(ImportExportModelAdmin):
    resource_class = serviceResource
    list_display = ['bussiness', 'name', 'comments', 'update_time']
    list_filter = ['bussiness']
    ordering = ('name',)
