from django.test import TestCase, LiveServerTestCase
from django.core.urlresolvers import reverse
from .models import Author
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class AuthorsViewsTest(TestCase):
    fixtures = ['users', 'authors_data']

    def setUp(self):
        self.client.login(username='ssokmen', password='12345')

    def test_author_list(self):
        """
        Tests author list view
        """
        self.client.login(username='ssokmen', password='12345')
        response = self.client.get(reverse('author_list'))
        self.assertEqual(response.status_code, 200)

    def test_author_detail(self):
        """
        Tests author list view
        """
        author = Author.objects.get(id=1)
        response = self.client.get(reverse('author_detail', kwargs={'slug': author.slug}))
        self.assertEqual(response.status_code, 200)

    '''
    def test_author_create(self):
        """
        Tests author list view
        """
        author = Author.objects.create(name=u'New Author', user=self.session.user)
        response = self.client.get(reverse('author_detail', kwargs={'slug': author.slug}))
        self.assertEqual(response.status_code, 200)
    '''

'''
class SeleniumTests(LiveServerTestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/signin/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('ssokmen')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('12345')
        self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()
'''
