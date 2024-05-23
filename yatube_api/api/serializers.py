from rest_framework import serializers
from posts.models import (
    Post, Group, Comment
)


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('author', 'post')

    def get_author(self, obj):
        return obj.author.username


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('author', 'post')

    def get_author(self, obj):
        return obj.author.username
