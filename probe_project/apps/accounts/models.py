from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils.translation import ugettext as _
from guardian.shortcuts import assign_perm
# from social_auth.backends import facebook
# from social_auth.backends.contrib import github
from userena.models import UserenaLanguageBaseProfile, UserenaSignup
import json


class ProbeUserProfile(UserenaLanguageBaseProfile):
    user = models.OneToOneField(
        User,
        unique=True,
        verbose_name=_('user'),
        related_name='my_profile'
    )
