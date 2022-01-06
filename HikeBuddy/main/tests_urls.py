from django.test import TestCase ,Client
from main.views import areyousure,home,contact,planroute,findhost,myhostingplaces,createhostingplace,createHost,guideinfo,createGuide,editabout,saveabout,about,messagetouser
from django.urls import reverse, resolve
from main.forms import HostForm

class TestsURL(TestCase):

    def test_createhostingplace(self):
        response = self.client.get('/')
        self.assertNotEqual(response.status_code, 404)

    def test_homepage(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, home)

    def test_contact(self):
        url = reverse('contact')
        self.assertEqual(resolve(url).func, contact)

    def test_areyousure(self):
        url = reverse('areyousure')
        self.assertEqual(resolve(url).func, areyousure)

    def test_planroute(self):
        url = reverse('planroute')
        self.assertEqual(resolve(url).func, planroute)

    def test_findhost(self):
        url = reverse('findhost')
        self.assertEqual(resolve(url).func, findhost)

    def test_myhostingplaces(self):
        url = reverse('myhostingplaces')
        self.assertEqual(resolve(url).func, myhostingplaces)

    def test_createhostingplace(self):
        url = reverse('createhostingplace')
        self.assertEqual(resolve(url).func, createhostingplace)

    def test_createHost(self):
        url = reverse('createHost')
        self.assertEqual(resolve(url).func, createHost)

    def test_guideinfo(self):
        url = reverse('guideinfo')
        self.assertEqual(resolve(url).func, guideinfo)

    def test_createGuide(self):
        url = reverse('createGuide')
        self.assertEqual(resolve(url).func, createGuide)

    def test_about(self):
        url = reverse('about')
        self.assertEqual(resolve(url).func, about)


    def test_editabout(self):
        url = reverse('editabout')
        self.assertEqual(resolve(url).func, editabout)


    def test_editabout(self):
        url = reverse('saveabout')
        self.assertEqual(resolve(url).func, saveabout)








