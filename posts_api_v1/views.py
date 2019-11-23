from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework import permissions

from .permissions import IsOwnerOrReadOnly

from .serializers import PostSerializer

from main_page.models import Post


class PostListView(ListCreateAPIView):
    queryset = Post.objects.all().select_related('author__profile')
    serializer_class = PostSerializer
    name = 'post-list'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all().select_related('author__profile')
    serializer_class = PostSerializer
    name = 'post-detail'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    )

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)
