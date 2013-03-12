from django.test import TestCase
from django.core.urlresolvers import reverse


class AuthorsViewsTest(TestCase):
    fixtures = ['users']

    def test_author_list(self):
        """
        Tests author list view
        """

        response = self.client.get(reverse('author_list'))
        self.assertEqual(response.status_code, 200)
