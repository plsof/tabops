from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from bstype.models import service_type


@admin.register(service_type)
class serviceAdmin(ImportExportModelAdmin):
    list_display = ['bussiness', 'name', 'comments', 'update_time']
    list_filter = ['bussiness']
    ordering = ('name',)
