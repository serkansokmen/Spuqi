from django.contrib.auth.models import User
from django_select2.fields import AutoModelSelect2MultipleField


class MemberChoices(AutoModelSelect2MultipleField):
    queryset = User.objects.filter(pk__gt=-1)
    search_fields = ['username__icontains', ]
