from unidecode import unidecode
from django.template.defaultfilters import slugify as slgfy


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
