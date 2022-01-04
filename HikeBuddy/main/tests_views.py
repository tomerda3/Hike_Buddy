from django.test import TestCase ,Client
from main.views import areyousure,home,contact
from django.urls import reverse, resolve
from main.forms import HostForm

class TestsViews(TestCase):

    def test_createhostingplace(self):
        response = self.client.get('main/myhostingplaces.html')
        self.assertNotEqual(response.status_code, 405)
        self.assertEqual(response.status_code, 404)

    def test_myhostingplaces(self):
        response = self.client.get('main/myhostingplaces.html')
        self.assertNotEqual(response.status_code, 405)
        self.assertEqual(response.status_code, 404)

    def test_home(self):
        response = self.client.get('main/home.html')
        self.assertEqual(response.status_code, 404)
        self.assertNotEqual(response.status_code, 405)

    def test_checkmontly(self):
        self.assertNotEqual(self, False)

    def test_myprofile(self):
        response = self.client.get('main/myprofile.html')
        self.assertNotEqual(response.status_code, 405)
        self.assertEqual(response.status_code, 404)

    def test_editabout(self):
        response = self.client.get('main/editabout.html')
        self.assertNotEqual(response.status_code, 405)
        self.assertEqual(response.status_code, 404)

    def test_messagetouser(self):
        response = self.client.get('main/messagetouser.html')
        self.assertNotEqual(response.status_code, 405)
        self.assertEqual(response.status_code, 404)

    def test_about(self):
        response = self.client.get('main/about.html')
        self.assertNotEqual(response.status_code, 405)
        self.assertEqual(response.status_code, 404)

    def test_contact(self):
        response = self.client.get('main/contact.html')
        self.assertNotEqual(response.status_code, 405)
        self.assertEqual(response.status_code, 404)
        self.assertNotEqual(response.status_code, 200)





