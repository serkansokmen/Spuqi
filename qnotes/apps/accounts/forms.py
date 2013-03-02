from django.contrib.auth.models import User
from django_select2.fields import AutoModelSelect2Field, AutoModelSelect2MultipleField


class MemberChoices(AutoModelSelect2Field):
    queryset = User.objects.filter(pk__gt=-1)
    search_fields = ['username__icontains', ]


class MemberMultipleChoices(AutoModelSelect2MultipleField):
    queryset = User.objects.filter(pk__gt=-1)
    search_fields = ['username__icontains', ]
