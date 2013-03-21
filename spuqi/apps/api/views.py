from django.contrib.auth import get_user_model
from apps.accounts.permissions import IsOwnerOrReadOnly
from apps.authors.models import Author
from .serializers import UserSerializer, AuthorSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('siteuser-list', request=request, format=format),
        'authors': reverse('author-list', request=request, format=format),
    })


class UserList(generics.ListAPIView):
    model = get_user_model()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserDetail(generics.RetrieveAPIView):
    model = get_user_model()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


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
