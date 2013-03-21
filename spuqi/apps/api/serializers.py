from django.contrib.auth import get_user_model
from apps.authors.models import Author
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    avatar = serializers.Field(source='get_avatar_url')
    # authors = serializers.HyperlinkedRelatedField(many=True, view_name='author-detail')

    class Meta:
        model = get_user_model()
        fields = ('url', 'username', 'email', 'avatar')


class AuthorSerializer(serializers.HyperlinkedModelSerializer):

    owner = serializers.Field(source='user.username')

    class Meta:
        model = Author
        fields = ('url', 'name', 'owner',)
