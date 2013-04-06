import pyisbn
import googlebooks
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext as _
from .permissions import (
    IsOwnerOrReadOnly,
    IsPublicQuote,
)
from .serializers import (
    UserSerializer,
    AuthorSerializer,
    SourceSerializer,
    CollectionSerializer,
    QuoteSerializer,
)
from apps.sources.models import Source
from apps.authors.models import Author
from apps.collections.models import Collection
from apps.quotes.models import Quote
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


googlebooks_api = googlebooks.Api()


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse(
            'siteuser-list',
            request=request, format=format),
        'authors': reverse(
            'author-list',
            request=request, format=format),
        'sources': reverse(
            'source-list',
            request=request, format=format),
        'collections': reverse(
            'collection-list',
            request=request, format=format),
        'quotes': reverse(
            'quote-list',
            request=request, format=format),
        'search': reverse(
            'search',
            request=request, format=format),
    })


class UserList(generics.ListAPIView):
    model = get_user_model()
    serializer_class = UserSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )


class UserDetail(generics.RetrieveAPIView):
    model = get_user_model()
    serializer_class = UserSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )


class AuthorList(generics.ListCreateAPIView):
    model = Author
    serializer_class = AuthorSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )

    def pre_save(self, instance):
        instance.user = self.request.user


class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Author
    serializer_class = AuthorSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )

    def pre_save(self, instance):
        instance.user = self.request.user


@api_view(['GET'])
def search(request):
    results = {
        'sources': {},
        'error': {},
    }

    title = request.QUERY_PARAMS.get('title', False)
    if title:
        sources = Source.objects.filter(title__icontains=title)
        source_serializer = SourceSerializer(sources, many=True)
        results['sources']['spuqi'] = source_serializer.data

    isbn_str = request.QUERY_PARAMS.get('isbn', False)
    if isbn_str:
        try:
            isbn = pyisbn.Isbn(isbn_str)
        except pyisbn.IsbnError:
            results['error'] = {
                'message': _('ISBN number must contain only digit-numbers'),
            }
        else:
            if not isbn.validate():
                results['error'] = {
                    'message': _('A valid ISBN number is required')
                }
            #try:
            results['sources']['googlebooks'] = googlebooks_api.list(
                'isbn:%s' % isbn)['items']
            # except ConnectionError:
            #     results.errors.append(_('Could not connect to Google Book API'))

    return Response({"results": results})


class SourceList(generics.ListCreateAPIView):
    model = Source
    serializer_class = SourceSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )

    def pre_save(self, instance):
        instance.user = self.request.user


class SourceDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Source
    serializer_class = SourceSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )

    def pre_save(self, instance):
        instance.user = self.request.user


class CollectionList(generics.ListCreateAPIView):
    model = Collection
    serializer_class = CollectionSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )

    def pre_save(self, instance):
        instance.user = self.request.user


class CollectionDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Collection
    serializer_class = CollectionSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )

    def pre_save(self, instance):
        instance.user = self.request.user


class QuoteList(generics.ListCreateAPIView):
    model = Quote
    serializer_class = QuoteSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def pre_save(self, instance):
        instance.user = self.request.user

    def get_queryset(self):
        wanted_quotes = set()
        # authenticated user's PRIVATE Quote objects
        if self.request.user.is_authenticated():
            for quote in Quote.objects.filter(
                user=self.request.user, privacy_state=Quote.PRIVATE
            ):
                wanted_quotes.add(quote.pk)
        # OPEN and READ_ONLY Quote objects
        for quote in Quote.objects.exclude(privacy_state=Quote.PRIVATE):
            wanted_quotes.add(quote.pk)

        # exclude private quotes
        return Quote.objects.filter(id__in=wanted_quotes)


class QuoteDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Quote
    serializer_class = QuoteSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsPublicQuote,
    )

    def pre_save(self, instance):
        instance.user = self.request.user
