from django.test import TestCase ,Client
from main.views import areyousure,home,contact
from django.urls import reverse, resolve
from main.forms import HostForm

class TestsViews(TestCase):

    def test_createhostingplace(self):
        response = self.client.get('/')
        self.assertNotEqual(response.status_code, 404)
