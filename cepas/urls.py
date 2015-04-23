<<<<<<< HEAD
from django.conf.urls import patterns, include, url
=======
rom django.conf.urls import patterns, include, url
>>>>>>> 35eafb83f59a61c99a6b96673dff6304dc272aa2
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

admin.site.site_header = 'CONCILIO ARCA DE SALVACION'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cepas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'cepas.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'accounts/login/$', 'cepas.views.login', name='login')
)

urlpatterns += patterns('',
    url(r'static/(?P<path>.*)/$', 'django.views.static.serve', {'document_root:': settings.STATIC_ROOT,}),
)
