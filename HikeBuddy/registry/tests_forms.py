from django.test import SimpleTestCase
from registry.forms import UserForm,UserProfileInfoForm


class TestForms(SimpleTestCase):

    def test_UserForm(self):
        form = UserForm(data={
            'password': '123',
            'password_confirm': '123',
        })
        self.assertFalse(form.is_valid())

    def test_UserProfileInfoForm(self):
        form = UserProfileInfoForm(data={
            'userType': '1',
            'phone': '123',
            'picture': False,
        })
        self.assertTrue(form.is_valid())


    def test_UserForm2(self):
        form = UserForm(data={})
        self.assertFalse(form.is_valid())

    def test_UserProfileInfoForm2(self):
        form = UserForm(data={})
        self.assertFalse(form.is_valid())
