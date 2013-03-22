from django.test import TestCase
from apps.accounts.models import SiteUser


class AccountModelTest(TestCase):
    fixtures = ['accounts', ]
    '''
    def test_get_avatar_url(self):
        user_with_avatar = SiteUser.objects.get(pk=1)
        self.fail("TODO: get_avatar_url doesn't work when there is no image saved")
    '''
