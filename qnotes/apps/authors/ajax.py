from django.utils import simplejson
from django.db import IntegrityError
from apps.authors.forms import AuthorForm
from dajaxice.decorators import dajaxice_register
from dajaxice.utils import deserialize_form


@dajaxice_register(method='POST', name='authors.new')
def new_author(request, form):
    if not request.user.is_authenticated:
        return simplejson.dumps({
            'status': False,
            'message': 'Login required!'
        })
    form = AuthorForm(deserialize_form(form))
    if form.is_valid():
        try:
            author = form.save(commit=False)  # Could throw exception
            author.user = request.user
            author.save()
            return simplejson.dumps({
                'status': True,
                'author': {
                    'id': author.id,
                    'name': author.name
                }
            })
        except IntegrityError:
            return simplejson.dumps({
                'status': False,
                'message': 'Integrity Error!'
            })
    return simplejson.dumps({
        'status': False,
        'errors': form.errors
    })
