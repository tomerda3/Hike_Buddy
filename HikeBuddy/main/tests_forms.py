from django.test import SimpleTestCase
from main.forms import HostForm,GuideForm


class TestForms(SimpleTestCase):

    def test_HostForm(self):
        form = HostForm(data={
            'name': 'shai',
            'location': 'shai',
            'fireplace': True,
            'singleBeds': True,
            'doubleBeds': True,
            'freeWiFi': True,
            'showers': True,
            'electricity': True,
            'breakfast': True,
            'airConditioning': True,
            'parking': True,
            'bar': True,
            'picture': False

        })
        self.assertTrue(form.is_valid())

    def test_HostForm2(self):
        form = HostForm(data={})
        self.assertFalse(form.is_valid())

    def test_GuideForm(self):
        form3 = HostForm(data={
            'cost': 321.6556,
            'carryweapon': True,
            'medic': True,
            'transportationvehicle': True,

        })
        self.assertFalse(form3.is_valid())

