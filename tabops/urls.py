from django.conf.urls import url, include
from django.contrib import admin

from dashboard.sites import DashboardSite

admin.site = DashboardSite()
admin.sites.site = admin.site  # >= Django 1.9.5
admin.autodiscover()
urlpatterns = [
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls),
]
