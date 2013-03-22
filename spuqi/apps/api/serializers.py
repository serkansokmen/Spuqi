from django.contrib.auth import get_user_model
from apps.authors.models import Author
from apps.sources.models import Source
from apps.collections.models import Collection
from apps.quotes.models import Quote
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('url', 'username', 'email', 'avatar',)


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.Field(source='user.username')

    class Meta:
        model = Author
        fields = ('url', 'name',)


class SourceSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.Field(source='user.username')
    authors = serializers.HyperlinkedRelatedField(
        many=True, view_name='author-detail')

    class Meta:
        model = Source
        fields = ('url', 'title', 'authors', 'web_address', 'isbn',)


class CollectionSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.Field(source='user.username')
    members = serializers.HyperlinkedRelatedField(
        many=True, view_name='siteuser-detail')
    sources = serializers.HyperlinkedRelatedField(
        many=True, view_name='source-detail')

    class Meta:
        model = Collection
        fields = ('url', 'title', 'owner', 'members', 'sources',)


class QuoteSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.Field(source='user.username')
    source = serializers.HyperlinkedRelatedField(
        view_name='source-detail')
    privacy = serializers.Field(source='get_privacy_state_display')

    class Meta:
        model = Quote
        fields = ('url', 'privacy', 'quote', 'owner', 'source',)
