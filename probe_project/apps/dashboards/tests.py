import datetime
from django.test import TestCase
from probe_project.apps.dashboards.models import Datum
from probe_project.apps.probe_dispatcher.models import Probe,Sensor
from django.contrib.auth.models import User

# Create your tests here.


def create_user():
    user = User.objects.create_user(username="admin", email="test@test.com", password="root")

    return user


def create_probe(name, description, domain,is_enabled,sensors,user,hash=None):
    probe = Probe.objects.create(name=name,description=description,domain=domain,is_enabled=True,user=user)

    return probe



def create_sensor(name,code,user):
    sensor = Sensor.objects.create(name=name, code=code, user=user)

    return sensor

def create_datum(probeId,httpReferer,httpUserAgent,language,OS,slug,timestamp,user):
    datum = Datum.objects.create(probeId=probeId,httpReferer=httpReferer,httpUserAgent=httpUserAgent,language=language,
                                 OS=OS,slug=slug,timestamp=timestamp,user=user)

class DatumTestCase(TestCase):
    def test_list_Datum(self):

        user = create_user()

        sensor = create_sensor("name1", "code1", user)
        sensor2 = create_sensor("name2", "code2", user)

        probe1 = create_probe("Name1", "Description1", "www.cornipickle.org", True, sensor, user)
        probe2 = create_probe("Name2", "Description2", "www.cornipickle2.org", True, sensor2, user)

        datum1= create_datum(probe1,"httpReferer1","httpUserAgent1","language1","OS1","slug1",datetime.datetime.now(),user)
        datum2= create_datum(probe2,"httpReferer2","httpUserAgent2","language2","OS2","slug2",datetime.datetime.now(),user)



        self.assertEqual(len(Datum.objects.all()), 2)


    def test_create_Datum(self):
        user = create_user()

        sensor1 = create_sensor("name1", "code1", user)

        probe1 = create_probe("Name1", "Description1", "www.cornipickle.org", True, sensor1, user)

        datum1= create_datum(probe1,"httpReferer1","httpUserAgent1","language1","OS1","slug1",datetime.datetime.now(),user)


        self.assertEqual(datum1, Datum.objects.get(pk=datum1.id))


    def test_update_Datum(self):
        user = create_user()

        sensor1 = create_sensor("test1", "code1", user)

        probe1 = create_probe("Name1", "Description1", "www.cornipickle.org", True, sensor1, user)

        datum1= create_datum(probe1,"httpReferer1","httpUserAgent1","language1","OS1","slug1",datetime.datetime.now(),user)


        datum_update = Datum.objects.get(pk=probe1.id)

        self.assertEqual(probe1, datum_update)


    def test_delete_Probe(self):
        user = create_user()

        sensor1 = create_sensor("name1", "code1", user)

        probe1 = create_probe("Name1", "Description1", "www.cornipickle.org", True, sensor1, user)

        datum1= create_datum(probe1,"httpReferer1","httpUserAgent1","language1","OS1","slug1",datetime.datetime.now(),user)

        delete_datum = datum1.delete()

        self.assertEqual(delete_datum, None)
