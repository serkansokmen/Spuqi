from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from apps.helpers.models import TimeStampedModel
from libs.utils import slugify


class Topic(TimeStampedModel):
    user = models.ForeignKey(User)
    title = models.CharField(_('Title'), max_length=25)
    slug = models.SlugField(max_length=25, editable=False, blank=True, null=True)

    class Meta:
        ordering = ['title']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Topic, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('topic_detail', kwargs={'slug': self.slug})
