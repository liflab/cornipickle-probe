
from django.utils import timezone
from django.test import TestCase
from .models import Probe,Sensor
from django.contrib.auth.models import User

def create_user():
    user = User.objects.create_user(username="admin", email="test@test.com", password="root")

    return user


def create_sensor(name,code,user):
    sensor = Sensor.objects.create(name=name, code=code, user=user)

    return sensor

def create_probe(name, description, domain,is_enabled,sensors,user,hash=None):
    probe = Probe.objects.create(name=name,description=description,domain=domain,is_enabled=True,user=user)

    return probe

class ProbeTests(TestCase):
    def test_list_Probe(self):
        user = create_user()

        sensor = create_sensor("name1","code1",user)
        sensor2 = create_sensor("name2","code2",user)

        probe1 = create_probe("Name1","Description1","www.cornipickle.org",True,sensor,user)
        probe2 = create_probe("Name2","Description2","www.cornipickle2.org",True,sensor2,user)

        self.assertEqual(len(Probe.objects.all()),2)

    def test_create_Probe(self):
        user = create_user()

        sensor1 = create_sensor("name1","code1",user)

        probe = create_probe("Name1","Description1","www.cornipickle.org",True,sensor1,user)

        self.assertEqual(probe,Probe.objects.get(pk=probe.id))
    def test_update_Probe(self):

        user = create_user()

        sensor = create_sensor("test1","code1",user)

        probe1 = create_probe("Name1", "Description1", "www.cornipickle.org", True, sensor, user)

        probe_update = Probe.objects.get(pk=probe1.id)

        self.assertEqual(probe1,probe_update)

    def test_delete_Probe(self):
        user = create_user()

        sensor = create_sensor("name1","code1",user)

        probe1 = create_probe("Name1", "Description1", "www.cornipickle.org", True, sensor, user)

        delete_probe = probe1.delete()

        self.assertEqual(delete_probe,None)

    def test_delete_Probe_with_Sensor(self):
        pass




class SensorTests(TestCase):
    def test_list_Sensor(self):
        """
        Test for a list of Sensor
        :return:
        """

        user = create_user()
        list_sensor = []

        sensor1 = create_sensor("test1","code1",user)
        list_sensor.append(sensor1)
        sensor2= create_sensor("test2","code2",user)
        list_sensor.append(sensor2)

        self.assertEqual(len(list_sensor),2)


    def test_create_Sensor(self):
        """
        Test for a created Sensor
        :return:
        """

        user = create_user()

        code_mouse_event = "The event is attached to its target through the # attribute \"event\". Its value is the event\'s type We say that I click on Go when ( There exists $b in $(button) such that ( ($b\'s text is \"Go\") And ($b's event is \"mouseup\") ) ). We say that the textbox is empty when ( For each $t in $(#textbox) ( $t\'s text is \"\" ) )."
        sensor = create_sensor("Mouse_event",code_mouse_event,user)

        self.assertEqual(sensor,sensor)

    def test_update_Sensor(self):
        """
        Test for a update Sensor
        :return:
        """

        user = create_user()

        sensor = create_sensor("test1","code1",user)

        sensor1 = Sensor.objects.filter(pk=sensor.id).update(name="Update_test",code="update_code_cornipickle")

        self.assertEqual(sensor,Sensor.objects.get(pk=sensor1))

    def test_delete_Sensor(self):
        """
        Test for a Delete Sensor
        :return:
        """
        user = create_user()

        sensor = create_sensor("test1","code1",user)

        delete_sensor = sensor.delete()

        self.assertEqual(delete_sensor,None)



