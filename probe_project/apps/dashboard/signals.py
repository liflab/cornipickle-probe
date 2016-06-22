from django.db.models.signals import pre_save
import datetime
import django.dispatch
from django.shortcuts import get_object_or_404
from probe_project.apps.probe_dispatcher.models import Probe
from probe_project.apps.dashboard.models import Datum
from django.contrib.auth.models import User



# Signal object

cornipickle_verdict_false = django.dispatch.Signal(providing_args=['probe','response','user'])

# Cette function est un souscripteur. Elle va revecoir les signaux
def add_verdict_to_dashboard(sender,**kwargs):
    probe = kwargs['probe']
    default_user = kwargs['user']
    response = kwargs['response']
    # if exist
    currentProbe = get_object_or_404(Probe, pk=probe)
    user = User.objects.get(username=response['USER'])

    add_datum = Datum.objects.create(user=user,probeId_id=probe,timestamp=datetime.datetime.now(),
                      OS=response['SESSION'],httpReferer=response['HTTP_REFERER'],httpUserAgent=response['HTTP_USER_AGENT'],
                      language=response['LANGUAGE'],slug='')


# L'Object Signal est maintenant connecter avec la fonction add_verdict_to_dashboard
cornipickle_verdict_false.connect(add_verdict_to_dashboard)



