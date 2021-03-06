from django.shortcuts import (
    render,
    get_object_or_404
)
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Post
from django.contrib.auth.models import User


class PostListView(ListView):
    model = Post
    template_name = 'main_page/main.html'
    queryset = Post.objects.select_related('author__profile') \
        .only('author__username', 'title', 'content', 'date_posted', 'author__profile__profile_image')
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'main_page/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).select_related('author__profile') \
            .only('author__username', 'title', 'content', 'date_posted', 'author__profile__profile_image')\
            .order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    queryset = Post.objects.select_related('author__profile') \
        .only('author__username', 'title', 'content', 'date_posted', 'author__profile__profile_image')


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'main_page/about.html', {'title': 'About page'})
