from django.test import TestCase, LiveServerTestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .models import Author
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class AuthorsViewsTest(TestCase):
    fixtures = ['users', 'authors_data']

    def setUp(self):
        self.client.login(username='ssokmen', password='12345')

    def test_author_list_view(self):
        # request user is uthenticated
        self.assertIn('_auth_user_id', self.client.session)
        # go to author_list url
        response = self.client.get(reverse('author_list'))
        # server response is OK
        self.assertEqual(response.status_code, 200)
        # rendered with right template
        # has author_list in context

    def test_author_detail_view(self):
        self.assertIn('_auth_user_id', self.client.session)
        # self.assertEqual(self.client.session['_auth_user_id'], user.pk)
        author = Author.objects.get(id=1)
        response = self.client.get(reverse(
            'author_detail',
            kwargs={'slug': author.slug}))
        self.assertEqual(response.status_code, 200)
    '''
    def test_author_create_view(self):
        user = User.objects.get(pk=self.client.session['_auth_user_id'])
        author = Author.objects.create(name=u'New Author', user=user)

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
