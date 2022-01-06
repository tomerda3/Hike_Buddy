from django.test import TestCase, Client
from registry.models import UserProfileInfo
import json
from django.urls import reverse, resolve



class TestViews(TestCase):


    def test_signup(self):
        client = Client()
        response = client.get('signup')
        self.assertEquals(response.status_code,404)


