from django.contrib.auth import get_user_model
from apps.authors.models import Author
from apps.sources.models import Source
from apps.collections.models import Collection
from apps.quotes.models import Quote
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('url', 'username', 'first_name', 'last_name', 'avatar',)


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.Field(source='user.username')

    class Meta:
        model = Author
        fields = ('url', 'name',)


'''
class SourceSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.Field(source='user.username')
    # authors = serializers.HyperlinkedRelatedField(
    #     many=True, view_name='author-detail')

    class Meta:
        model = Source
        fields = ('url', 'title', 'authors', 'web_address', 'isbn',)
'''


class SourceSerializer(serializers.ModelSerializer):
    owner = serializers.Field(source='user.username')
    text = serializers.Field(source='title')
    authors = serializers.HyperlinkedRelatedField(
        many=True, view_name='author-detail')

    class Meta:
        model = Source
        fields = ('id', 'text', 'authors', 'web_address', 'isbn',)


class CollectionSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.Field(source='user.username')

    class Meta:
        model = Collection
        fields = ('url', 'title', 'owner', 'members', 'sources',)


class QuoteSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.Field(source='user.username')
    # owner_avatar

    class Meta:
        model = Quote
        fields = ('url', 'privacy_state', 'quote',
                  'owner', 'source',)
        depth = 0
