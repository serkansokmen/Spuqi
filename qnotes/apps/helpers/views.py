from django.core.urlresolvers import reverse


class FormNextMixin(object):

    def get_success_url(self):
        if 'next' in self.request.GET:
            return self.request.GET['next']
        else:
            return reverse(self.success_url)
