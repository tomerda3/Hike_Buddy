from django.test import TestCase, Client
from registry.models import UserProfileInfo
import json


class TestViews(TestCase):
    def test_weather(self):
        client = Client()
        response = client.get('weather')
        self.assertEquals(response.status_code, 404)