from django.db import models
from django.utils.translation import ugettext as _
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from apps.helpers.models import TimeStampedModel


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(TimeStampedModel, models.Model):

    title = models.CharField(max_length=100, blank=True, default=u'')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(
        choices=LANGUAGE_CHOICES,
        default='python',
        max_length=100
    )

    class Meta:
        verbose_name = _('Snippet')
        verbose_name_plural = _('Snippets')
        ordering = ('created',)

    def __unicode__(self):
        pass
