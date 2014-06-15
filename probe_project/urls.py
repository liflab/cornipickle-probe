from django.conf.urls import patterns
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf.urls import include, url
from oscar.app import shop
from probe_project import views as probe_views
from custom_userena_urls import urlpatterns as custom_userena_urls
from userena import views as userena_views

from userena.forms import SignupFormTos

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', probe_views.home, name="home"),
                       url(r'^dashboard/', include('probe_project.apps.probe_dispatcher.urls')),

                       # probe file url
                       url(r'^p/(?P<probe_id>\d+)_(?P<probe_hash>[0-9a-fA-F]{40}).js$',
                           'probe_project.apps.probe_dispatcher.views.probe_file',
                           name="probe"),

                       # rest_framework
                       url(r'^api/?', include('rest_framework.urls', namespace='rest_framework')),

                       # localeurl (language selection)
                       (r'^localeurl/', include('localeurl.urls')),

                       # django admin
                       url(r'^admin/', include(admin.site.urls), name='administration'),

                       # userena
                       url(r'^', include(custom_userena_urls)),

                       # oscar
                       url(r'^oscar/', shop.urls),

                       # Social Auth
                       url(r'social/', include('social_auth.urls')),

)

if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'uploads/(?P<path>.*)$', 'django.views.static.serve',
                                {'document_root': settings.MEDIA_ROOT}),
    )