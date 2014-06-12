from django.conf.urls import patterns
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf.urls import include, url
from django.http import HttpResponseRedirect
from oscar.app import shop
from probe_project import views as probe_views
from userena import views as userena_views

from userena.forms import SignupFormTos


def logout_required(view):
    def f(request, *args, **kwargs):
        if request.user.is_anonymous():
            return view(request, *args, **kwargs)
        return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

    return f


admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', probe_views.home, name="home"),
                       url(r'^dashboard/', include('probe_project.apps.probe_dispatcher.urls')),

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

                       # userena
                       url(r'^logout/$', userena_views.signout, {'next_page': '/'}, name='logout'),
                       # don't show signin if logged in
                       url(r'^signin/$', logout_required(userena_views.signin)),
                       # userena use Tos form instead
                       url(r'^signup/$', logout_required(userena_views.signup)),# {'signup_form': SignupFormTos}),
                       (r'^', include('userena.urls')),

                       # oscar
                       (r'^oscar/', shop.urls),
)

if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'uploads/(?P<path>.*)$', 'django.views.static.serve',
                                {'document_root': settings.MEDIA_ROOT}),
    )