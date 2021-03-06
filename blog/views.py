from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View, CreateView, ListView, YearArchiveView, MonthArchiveView, ArchiveIndexView, DateDetailView, DeleteView, DetailView

from .models import Post
from .forms import PostForm
from .utils import DateObjectMixin, AllowFuturePermissionMixin, PostFormValidMixin
from core.utils import UpdateView

from user.decorators import \
    require_authenticated_permission

# Create your views here.
class PostList(AllowFuturePermissionMixin, ArchiveIndexView):
    allow_empty = True
    context_object_name = 'post_list'
    date_field = 'pub_date'
    make_object_list = True
    model = Post
    paginate_by = 5
    template_name = 'blog/post_list.html'
"""
    def get(self, request):
        return render(request, 'blog/post_list.html', {'post_list': Post.objects.all()})
"""
"""
def post_list(request):
    return render(request, 'blog/post_list.html', {'post_list': Post.objects.all()})


"""
"""
def post_detail(request, year, month, slug):
    post = get_object_or_404(Post, pub_date__year=year, pub_date__month=month, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})
"""
class PostDetail(DateObjectMixin, DetailView):
    date_field = 'pub_date'
    queryset = (Post.objects.select_related('author__profile').prefetch_related('startups').prefetch_related('tags'))
    #model = Post

@require_authenticated_permission('blog.add_post')
class PostCreate(PostFormValidMixin, CreateView):
    form_class = PostForm
    model = Post
"""
    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        else:
            return render(request, self.template_name, {'form': bound_form})
"""

@require_authenticated_permission('blog.change_post')
class PostUpdate(PostFormValidMixin, DateObjectMixin, UpdateView):
    date_field = 'pub_date'
    form_class = PostForm
    model = Post
"""
    template_name = 'blog/post_form_update.html'

    def get_object(self, year, month, slug):
        return get_object_or_404(
            self.model,
            pub_date__year=year,
            pub_date__month=month,
            slug=slug)

    def get(self, request, year, month, slug):
        post = self.get_object(year, month, slug)
        context = {
            'form': self.form_class(
                instance=post),
            'post': post,
        }
        return render(
            request, self.template_name, context)

    def post(self, request, year, month, slug):
        post = self.get_object(year, month, slug)
        bound_form = self.form_class(
            request.POST, instance=post)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        else:
            context = {
                'form': bound_form,
                'post': post,
            }
            return render(
                request,
                self.template_name,
                context)
"""

@require_authenticated_permission('blog.delete_post')
class PostDelete(DateObjectMixin, DeleteView):
    date_field = 'pub_date'
    model = Post
    success_url = reverse_lazy('blog_post_list')
"""
    def get(self, request, year, month, slug):
        post = get_object_or_404(Post, pub_date__year=year, pub_date__month=month, slug__iexact=slug)
        return render(request, 'blog/post_confirm_delete.html', {'post': post})

    def post(self, request, year, month, slug):
        post = get_object_or_404(Post, pub_date__year=year, pub_date__month=month, slug__iexact=slug)
        post.delete()
        return redirect('blog_post_list')
"""

class PostArchiveYear(AllowFuturePermissionMixin, YearArchiveView):
    model = Post
    date_field = 'pub_date'
    make_object_list = True

class PostArchiveMonth(AllowFuturePermissionMixin, MonthArchiveView):
    model = Post
    date_field = 'pub_date'
    month_format = '%m'
