from rest_framework import serializers

from django.contrib.auth.models import User
from main_page.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ('id',
                  "title",
                  "content",
                  "date_posted",
                  "author"
                  )
        ordering = ('date_posted')
