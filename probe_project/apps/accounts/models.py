from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils.translation import ugettext as _
from guardian.shortcuts import assign_perm
# from social_auth.backends import facebook
# from social_auth.backends.contrib import github
from userena.models import UserenaLanguageBaseProfile, UserenaSignup


class ProbeUserProfile(UserenaLanguageBaseProfile):
    user = models.OneToOneField(
        User,
        unique=True,
        verbose_name=_('user'),
        related_name='my_profile'
    )


# todo: try to do somethign with this
# stuff taken from https://gist.github.com/zvictor/1351169

from social_auth.signals import socialauth_registered as profile_connect
from userena.managers import ASSIGNED_PERMISSIONS

#
# @receiver(profile_connect, sender=facebook, dispatch_uid='facebook.connect')
# def facebook_connect_callback(sender, user, profile, client, **kwargs):
#     """
#     Create a profile for this user after connecting
#
#     """
#     # Create a userena user.
#     # TODO: You could make it prettier by setting a ``activation_key`` of ``ALREADY_ACTIVATED``
#     # and looking at good values for the other fields of the model.
#     userenaSignup = UserenaSignup.objects.get_or_create(user=user)
#
#     # Create profile for user
#     try:
#         new_profile = ProbeUserProfile.objects.get(user=user)
#     except:
#         new_profile = ProbeUserProfile.objects.create(user=user)
#
#     # Give permissions to view and change profile
#     for perm in ASSIGNED_PERMISSIONS['profile']:
#         assign_perm(perm[0], user, new_profile)
#
#     # Give permissions to view and change itself
#     for perm in ASSIGNED_PERMISSIONS['user']:
#         assign_perm(perm[0], user, user)
#
#
# @receiver(profile_connect, sender=github, dispatch_uid='facebook.connect')
# def github_connect_callback(sender, user, profile, client, **kwargs):
#     """
#     Create a profile for this user after connecting
#
#     """
#     # Create a userena user.
#     # TODO: You could make it prettier by setting a ``activation_key`` of ``ALREADY_ACTIVATED``
#     # and looking at good values for the other fields of the model.
#     userenaSignup = UserenaSignup.objects.get_or_create(user=user)
#
#     # Create profile for user
#     try:
#         new_profile = ProbeUserProfile.objects.get(user=user)
#     except:
#         new_profile = ProbeUserProfile.objects.create(user=user)
#
#     # Give permissions to view and change profile
#     for perm in ASSIGNED_PERMISSIONS['profile']:
#         assign_perm(perm[0], user, new_profile)
#
#     # Give permissions to view and change itself
#     for perm in ASSIGNED_PERMISSIONS['user']:
#         assign_perm(perm[0], user, user)