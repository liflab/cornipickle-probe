from django.conf.urls import *
from django.contrib.auth.decorators import login_required
from decorators import logout_required
from django.contrib.auth import views as auth_views

from userena import settings as userena_settings
from userena.compat import auth_views_compat_quirks, password_reset_uid_kwarg
from userena import views as userena_views


def merged_dict(dict_a, dict_b):
    """Merges two dicts and returns output. It's purpose is to ease use of
    ``auth_views_compat_quirks``
    """
    dict_a.update(dict_b)
    return dict_a


urlpatterns = patterns('',
                       # Signup, signin and signout
                       url(r'^signup/$',
                           logout_required(userena_views.signup),
                           name='userena_signup'),
                       url(r'^signin/(?P<next>.*)/$',
                           logout_required(userena_views.signin),
                           name='userena_signin'),
                       url(r'^signin/$',
                           logout_required(userena_views.signin),
                           name='userena_signin'),
                       url(r'^signout/$',
                           login_required(userena_views.signout),
                           name='userena_signout'),
                       url(r'^signout/(?P<next>.*)/$',
                           login_required(userena_views.signout),
                           name='userena_signout'),

                       # Reset password
                       url(r'^accounts/password/reset/$',
                           auth_views.password_reset,
                           merged_dict({'template_name': 'userena/password_reset_form.html',
                                        'email_template_name': 'userena/emails/password_reset_message.txt',
                                        'extra_context': {
                                            'without_usernames': userena_settings.USERENA_WITHOUT_USERNAMES}
                                       }, auth_views_compat_quirks['userena_password_reset']),
                           name='userena_password_reset'),
                       url(r'^accounts/password/reset/done/$',
                           auth_views.password_reset_done,
                           {'template_name': 'userena/password_reset_done.html', },
                           name='userena_password_reset_done'),
                       url(r'^accounts/password/reset/confirm/(?P<%s>[0-9A-Za-z]+)-(?P<token>.+)/$' % password_reset_uid_kwarg,
                           auth_views.password_reset_confirm,
                           merged_dict({'template_name': 'userena/password_reset_confirm_form.html',
                                       }, auth_views_compat_quirks['userena_password_reset_confirm']),
                           name='userena_password_reset_confirm'),
                       url(r'^accounts/password/reset/confirm/complete/$',
                           auth_views.password_reset_complete,
                           {'template_name': 'userena/password_reset_complete.html'},
                           name='userena_password_reset_complete'),

                       # Signup
                       url(r'^accounts/(?P<username>[\.\w-]+)/signup/complete/$',
                           logout_required(userena_views.direct_to_user_template),
                           {'template_name': 'userena/signup_complete.html',
                            'extra_context': {
                                'userena_activation_required': userena_settings.USERENA_ACTIVATION_REQUIRED,
                                'userena_activation_days': userena_settings.USERENA_ACTIVATION_DAYS}},
                           name='userena_signup_complete'),

                       # Activate
                       url(r'^accounts/activate/(?P<activation_key>\w+)/$',
                           userena_views.activate,
                           name='userena_activate'),

                       # Retry activation
                       url(r'^accounts/activate/retry/(?P<activation_key>\w+)/$',
                           userena_views.activate_retry,
                           name='userena_activate_retry'),

                       # Change email and confirm it
                       url(r'^accounts/(?P<username>[\.\w-]+)/email/$',
                           userena_views.email_change,
                           name='userena_email_change'),
                       url(r'^accounts/(?P<username>[\.\w-]+)/email/complete/$',
                           userena_views.direct_to_user_template,
                           {'template_name': 'userena/email_change_complete.html'},
                           name='userena_email_change_complete'),
                       url(r'^accounts/(?P<username>[\.\w-]+)/confirm-email/complete/$',
                           userena_views.direct_to_user_template,
                           {'template_name': 'userena/email_confirm_complete.html'},
                           name='userena_email_confirm_complete'),
                       url(r'^accounts/confirm-email/(?P<confirmation_key>\w+)/$',
                           userena_views.email_confirm,
                           name='userena_email_confirm'),

                       # Disabled account
                       url(r'^accounts/(?P<username>[\.\w-]+)/disabled/$',
                           userena_views.disabled_account,
                           {'template_name': 'userena/disabled.html'},
                           name='userena_disabled'),

                       # Change password
                       url(r'^accounts/(?P<username>[\.\w-]+)/password/$',
                           userena_views.password_change,
                           name='userena_password_change'),
                       url(r'^accounts/(?P<username>[\.\w-]+)/password/complete/$',
                           userena_views.direct_to_user_template,
                           {'template_name': 'userena/password_complete.html'},
                           name='userena_password_change_complete'),

                       # Edit profile
                       url(r'^accounts/(?P<username>[\.\w-]+)/edit/$',
                           userena_views.profile_edit,
                           name='userena_profile_edit'),

                       # View profiles
                       url(r'^accounts/(?P<username>(?!signout|signup|signin)[\.\w-]+)/$',
                           userena_views.profile_detail,
                           name='userena_profile_detail'),
                       url(r'^accounts/page/(?P<page>[0-9]+)/$',
                           userena_views.ProfileListView.as_view(),
                           name='userena_profile_list_paginated'),
                       url(r'^accounts/$',
                           userena_views.ProfileListView.as_view(),
                           name='userena_profile_list'),
)
