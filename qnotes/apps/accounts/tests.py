from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User


class ProfileDetailViewTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_should_display_mugshot(self):
        User.objects.create_user('ssokmen', 'ssokmen@local.host', '12345')
        #use test client to perform login
        user = self.client.login(username='ssokmen', password='12345')
        response = self.client.post('/accounts/ssokmen')
        print response
