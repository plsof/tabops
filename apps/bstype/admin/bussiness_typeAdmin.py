from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from bstype.models import bussiness_type


@admin.register(bussiness_type)
class bussinessAdmin(ImportExportModelAdmin):
    list_display = ['name', 'bs_type', 'comments', 'update_time']
    ordering = ('name',)

