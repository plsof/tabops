from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from kunlun.models import Vas


@admin.register(Vas)
class bussinessAdmin(ImportExportModelAdmin):
    list_display = ['idc', 'role', 'node', 'mode', 'update_time']
    ordering = ('role', 'node')
