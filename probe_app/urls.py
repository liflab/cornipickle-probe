from django.conf.urls import include, url, patterns
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext as _

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^', include('probe_dispatcher.urls')),
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(_(r'^register/$'), 'register', {'template_name': 'register.jinja2'}, name='register'),
)

urlpatterns += patterns('django.contrib.auth.views',
                        url(_(r'^login/$'), 'login', {'template_name': 'login.jinja2'}, name='login'),
                        url(_(r'^logout/$'), 'logout', {'next_page': '/'}, name='logout'),
)

urlpatterns += i18n_patterns('',
                             # url(r'^search/$', search, {}, name='search'),
                             url(r'^$', TemplateView.as_view(template_name="home.jinja2"), name="home"),

)

if settings.DEBUG:
    urlpatterns += i18n_patterns('',
                                 url(r'media/(?P<path>.*)$', 'django.views.static.serve',
                                     {'document_root': settings.MEDIA_ROOT}),
    )

