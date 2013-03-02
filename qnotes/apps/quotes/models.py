from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from qnotes.apps.sources.models import Source
from qnotes.apps.topics.models import Topic
from django.utils.translation import ugettext as _
from taggit.managers import TaggableManager
from fluent_comments.moderation import moderate_model
# , comments_are_open, comments_are_moderated
# from fluent_comments.models import get_comments_for_model, CommentsRelation


class Quote(models.Model):

    NOTE_TYPES = ((1, _('Text')), (2, _('Voice')), (3, _('Video')))

    user = models.ForeignKey(User)
    source = models.ForeignKey(Source, default=0, verbose_name=_('Source'))
    quote = models.TextField(_('Quote'), max_length=1200)
    note_type = models.PositiveIntegerField(_('Note type'), choices=NOTE_TYPES, blank=True, null=True)
    note = models.TextField(_('Note'), blank=True, max_length=500)
    topics = models.ManyToManyField(Topic, blank=True, verbose_name=_('Topics'))
    tags = TaggableManager(blank=True)
    is_private = models.BooleanField(_('Is private'), default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    enable_comments = models.BooleanField(_('Enable comments'), default=True)

    # Optional reverse relation, allow ORM querying:
    # comments_set = CommentsRelation()

    def __unicode__(self):
        return self.quote

    def get_absolute_url(self):
        return reverse('quote_detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super(Quote, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']

    # Optional, give direct access to moderation info via the model:
    # comments = property(get_comments_for_model)
    # comments_are_open = property(comments_are_open)
    # comments_are_moderated = property(comments_are_moderated)


moderate_model(
    Quote,
    publication_date_field='created_at',
    enable_comments_field='enable_comments',
)
