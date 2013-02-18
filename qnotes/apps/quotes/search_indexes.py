from haystack.indexes import *
from haystack import site
from qnotes.apps.quotes.models import Quote


class QuoteIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    title = CharField(model_attr='title')

    def get_model(self):
        return Quote

site.register(Quote, QuoteIndex)
