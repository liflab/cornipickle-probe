from django.conf.urls import include, url, patterns
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext as _

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from probe_app import views

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', views.home, name="home"),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', views.home, name="home"),
                       url(r'^dashboard/', include('probe_dispatcher.urls')),
                       url(_(r'^register/$'), views.register, {'template_name': 'register.jinja2'}, name='register'),
                       url(_(r'^login/$'), views.login, name='login'),
                       url(_(r'^logout/$'), views.logout, {'next_page': '/'}, name='logout'),
)

# urlpatterns += patterns('django.contrib.auth.views',
# )

urlpatterns += i18n_patterns('',
)

if settings.DEBUG:
    urlpatterns += i18n_patterns('',
                                 url(r'media/(?P<path>.*)$', 'django.views.static.serve',
                                     {'document_root': settings.MEDIA_ROOT}),
    )

