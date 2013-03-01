import sys
from decorator import decorator
from monkeypatch import monkeypatch
from pyaws import ecs
from unidecode import unidecode
from datetime import datetime
from django.template.defaultfilters import slugify as slgfy
from django.utils.translation import ugettext_lazy as _, ungettext


def remove_holddown(form, fields):
    """This removes the unhelpful "Hold down the...." help texts for the
    specified fields for a form."""
    remove_message = unicode(_('Hold down "Control", or "Command" on a Mac, to select more than one.'))
    for field in fields:
        if field in form.base_fields:
            if form.base_fields[field].help_text:
                form.base_fields[field].help_text = form.base_fields[field].help_text.replace(remove_message, '').strip()
    return form


IGNORED_WORDS = ['cd', 'mh', 'tr']


def slugify(s, max_length=50, max_words=None):
    if s == '':
        return s
    slug = slgfy(unidecode(s))
    # remove ignored words
    slug = '-'.join([w for w in slug.split('-') if w not in IGNORED_WORDS])
    while len(slug) > max_length:
        # try to shorten word by word
        temp = slug[:slug.rfind('-')]
        if len(temp) > 0:
            slug = temp
        else:
            # we have nothing left, do not apply the last crop, apply the cut-off directly
            slug = slug[:max_length]
            break
    if max_words:
        words = slug.split('-')[:max_words]
        slug = '-'.join(words)
    return slug


def get_diff_date(date):
    now = datetime.now()
    diff = now - date
    days = diff.days
    hours = int(diff.seconds / 3600)
    minutes = int(diff.seconds / 60)

    if days > 2:
        if date.year == now.year:
            return _(u'%(month)s %(day)s') % {'month': _(date.strftime('%B')),
                                              'day': date.strftime('%d')}
        else:
            return _(u"%(month)s %(day)s '%(year)s") % {'month': _(date.strftime('%B')),
                                                        'day': date.strftime('%d'),
                                                        'year': date.strftime('%y')}
    elif days == 2:
        return _('2 days ago')
    elif days == 1:
        return _('yesterday')
    elif minutes >= 60:
        return ungettext('%(hr)d hour ago', '%(hr)d hours ago', hours) % {'hr': hours}
    elif diff.seconds >= 60:
        return ungettext('%(min)d min ago', '%(min)d mins ago', minutes) % {'min': minutes}
    else:
        return _('just now')

# ins and outs
# these can be modified fairly extensively,
# to control exactly what the Amazon API pukes out
rs_fetch = """Request,ItemIds,Images,Tracks,Accessories,Small,Medium,Large,Variations,VariationImages,VariationMinimum,VariationSummary,TagsSummary,Tags,VariationMatrix,VariationOffers,ItemAttributes,SalesRank,Subjects,Reviews,EditorialReview,Collections,ShippingCharges,BrowseNodes"""  # holy shit
rs_search = """Request, ItemIds, Small, Medium, Large, ItemAttributes, Tracks, EditorialReview, SalesRank, Images"""


class Amazon:

    auth_init = False

    def __init__(self, ecsref=None):
        self.ecs = ecsref

    @decorator
    def ecsauth(f, *args, **kwargs):
        self = args[0]
        if not self.auth_init:
            self.ecs.setLicenseKey("YOUR_AWS_KEY")
            self.ecs.setSecretAccessKey("YOUR_SUPER_SECRET_AWS_PRIVATE_KEY")
            self.auth_init = True
        return f(self, *args, **kwargs)

    @ecsauth
    def search(*args, **kwargs):
        self = args[0]  # ugh
        search = kwargs.get('q', None)
        searchidx = kwargs.get('idx', 'Books')
        rsgroup = kwargs.get('rs', rs_search)
        aq = self.ecs.ItemSearch(search, SearchIndex=searchidx, ResponseGroup=rsgroup)
        aqout = []
        i = e = 0
        while i < 25:
            try:
                a = aq.next()
                i += 1
            except IndexError:
                e += 1
            except StopIteration:
                break
            else:
                aqout += [a]
        return aqout

    @ecsauth
    def fetch(self, *args, **kwargs):
        qid = '%s' % kwargs.get('qid', "-1")
        idtype = kwargs.get('idtype', 'ASIN')
        rsgroup = kwargs.get('rg', rs_fetch)
        idx = kwargs.get('idx', 'Books')
        aqout = []

        if idtype == "ASIN":
            idx = None
        qid = qid.replace('-', '')

        aq = self.ecs.ItemLookup("%s" % qid, IdType=idtype, SearchIndex=idx, ResponseGroup=rsgroup)

        i = e = 0
        while True:
            try:
                a = aq.next()
                i += 1
            except IndexError:
                e += 1
            except StopIteration:
                break
            else:
                aqout += [a]
        return aqout

aws = Amazon(ecs)
