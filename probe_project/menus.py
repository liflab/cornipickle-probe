from django.conf.urls import patterns
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf.urls import include, url
from oscar.app import shop
from probe_project import views as probe_views
from userena import views as userena_views

from userena.forms import SignupFormTos

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', probe_views.home, name="home"),
                       url(r'^dashboard/', include('probe_project.apps.probe_dispatcher.urls')),

                       # Login / register
                       # url(r'^register/$', userena_views.signup, name='register'),
                       # url(r'^login/$', userena_views.signin, name='login'),
                       url(r'^logout/$', userena_views.signout, {'next_page': '/'}, name='logout'),

                       # probe file url
                       url(r'^p/(?P<id>\d+)_(?P<hash>[0-9a-fA-F]{40}).js$',
                           'probe_project.apps.probe_dispatcher.views.probe_file',
                           name="probe"),

                       # rest_framework
                       url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),

                       # localeurl (language selection)
                       (r'^localeurl/', include('localeurl.urls')),

                       # django admin
                       url(r'^admin/', include(admin.site.urls), name='administration'),

                       # userena use Tos form instead
                       url(r'^accounts/signup/$', 'userena.views.signup', {'signup_form': SignupFormTos}),

                       # userena
                       (r'^accounts/', include('userena.urls')),

                       # oscar
                       (r'^oscar/', shop.urls),
)

if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'uploads/(?P<path>.*)$', 'django.views.static.serve',
                                {'document_root': settings.MEDIA_ROOT}),
    )

