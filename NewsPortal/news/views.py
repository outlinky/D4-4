from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Author
from .filters import NewsFilter
from .forms import PostForm


class PostList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        return context


class PostDetail(DetailView):
    model = Post
    context_object_name = 'new'
    template_name = 'post_detail.html'


class UserDetail(DetailView):
    model = Author
    template_name = 'post_detail.html'
    context_object_name = 'new'


class SearchList(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'news'
    paginate_by = 4

    def get_filter(self):
        return NewsFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *args, **kwargs):
        return {
            **super().get_context_data(*args, **kwargs),
            'filter': self.get_filter(),
        }


class PostCreate(CreateView):
    model = Post
    template_name = 'create_post.html'
    form_class = PostForm
    success_url = '/news/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

        return super().get(request, *args, **kwargs)


class PostUpdate(UpdateView):
    template_name = 'create_post.html'
    form_class = PostForm


    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDelete(DeleteView):
    template_name = 'delete_post.html'
    queryset = Post.objects.all()
    context_object_name = 'new'
    success_url = '/news/'
