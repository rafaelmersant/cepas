from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

from rest_framework.authtoken.views import obtain_auth_token

from administracion.views import IglesiasView, MiembrosView, PastoresView, PresbiterosView, ObrerosView, \
                                    MiembrosByNombreApellido, GrupoDigitadores, GrupoDigitadoresCreados

admin.autodiscover()

admin.site.site_header = 'CONCILIO ARCA DE SALVACION'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cepas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'cepas.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'accounts/login/$', 'cepas.views.login', name='login'),

    url(r'^iglesias/$', IglesiasView.as_view(), name='Iglesias'),
    url(r'^miembros/$', MiembrosView.as_view(), name='Miembros'),
    url(r'^pastores/$', PastoresView.as_view(), name='Pastores'),
    url(r'^presbiteros/$', PresbiterosView.as_view(), name='Presbiteros'),
    url(r'^obreros/$', ObrerosView.as_view(), name='Obreros'),

    url(r'^api/token/', obtain_auth_token, name='api-token'),
    url(r'^api/miembros/buscar/nombre-apellido/$', MiembrosByNombreApellido.as_view(), name='miembros_nombre_apellido'),
    url(r'^api/miembros/buscar/nombre-apellido/(?P<nombreApellido>[\w\s]+)/$', MiembrosByNombreApellido.as_view(), name='miembros_nombre_apellido'),

    url(r'^administracion/digitadores-modificados/$', GrupoDigitadores.as_view(), name='GrupoDigitadores'),
    url(r'^administracion/digitadores-creados/$', GrupoDigitadoresCreados.as_view(), name='GrupoDigitadoresCreados'),

)

urlpatterns += patterns('',
    url(r'static/(?P<path>.*)/$', 'django.views.static.serve', {'document_root:': settings.STATIC_ROOT,}),
)
