from django.template import Library
from django.utils.translation import ugettext as _
from libs.utils import get_diff_date
import datetime


register = Library()


@register.filter
def diff_date(date):
    if not date:
        return _("unknown")

    return get_diff_date(date)


@register.filter
def naturalday(value):
    today = datetime.date.today()
    value = datetime.date(value.year, value.month, value.day)
    delta = datetime.timedelta(days=1)
    if value == today:
        return _("today")
    elif value == today + delta:
        return _("tomorrow")
    elif value == today - delta:
        return _("yesterday")
    return _(value.strftime('%A'))
