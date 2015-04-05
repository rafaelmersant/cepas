from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

admin.site.site_header = 'CONCILIO ARCA DE SALVACION'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cepas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'cepas.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
