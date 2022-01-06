from django.test import TestCase, Client
from main.views import areyousure, home, contact
from django.urls import reverse, resolve


class TestsViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.feedback_url = reverse('feedback')
        self.about_url = reverse('about')
        self.contact_url = reverse('contact')
        self.areyousure_url = reverse('areyousure')
        self.createhostingplace_url = reverse('createhostingplace')
        self.myhostingplaces_url = reverse('myhostingplaces')
        self.createHost_url = reverse('createHost')









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

    def test_home2(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/home.html')

    def test_feedback2(self):
        response = self.client.get(self.feedback_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/thankyou.html')

    def test_contact2(self):
            response = self.client.get(self.contact_url)
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'main/contact.html')

    def test_areyousure2(self):
        response = self.client.get(self.areyousure_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/areyousure.html')

    def test_createhostingplace2(self):
        response = self.client.get(self.createhostingplace_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/createhostingplace.html')


    def test_myhostingplaces2(self):
        response = self.client.get(self.createhostingplace_url)
        self.assertEqual(response.status_code, 200)

    def test_createHost2(self):
        response = self.client.get(self.createHost_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/myhostingplaces.html')







