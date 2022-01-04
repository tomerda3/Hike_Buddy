from django.test import TestCase ,Client
from registry.views import signup
from django.urls import reverse, resolve
#from main.models import UserProfileInfo

# class TestsViews(TestCase):
#
#     def setUp(self):
#         User1= Client()
#         response = User1.get(reverse('list'))
#         self.assertEqual(response.status_code, 202)
#
#     def test_signup(self):
#         User1= Client()
#         response = User1.get(reverse('list'))
#         self.assertEqual(response.status_code, 202)
#         self.assertTemplateUsed(response,"registry/signup.html")