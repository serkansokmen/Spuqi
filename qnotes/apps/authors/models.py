from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from libs.utils import slugify
from django.utils.translation import ugettext as _


class Author(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(_('Name'), max_length=255, unique=True)
    slug = models.SlugField(editable=False, blank=True, null=True)

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Author, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('author_detail', kwargs={'slug': self.slug})