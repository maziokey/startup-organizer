from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import CreateView, DeleteView, DetailView, ListView
from core.utils import UpdateView
from .utils import PageLinksMixin, StartupContextMixin, NewsLinkGetObjectMixin
#from .utils import ObjectUpdateMixin, ObjectDeleteMixin, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from django.http.response import HttpResponse, Http404
#from django.template import Context, loader

from .models import Tag, Startup, NewsLink
from .forms import TagForm, StartupForm, NewsLinkForm

# Create your views here.
#def tag_list(request):
#    return render(request, 'organizer/tag_list.html', {'tag_list': Tag.objects.all()})

class TagList(PageLinksMixin, ListView):
    model = Tag
    paginate_by = 5
"""
    template_name = 'organizer/tag_list.html'

    def get(self, request):
        tags = Tag.objects.all()
        context = {
            'tag_list': tags,
        }
        return render(
            request, self.template_name, context)
"""
"""
class TagPageList(View):
    paginate_by = 5
    template_name = 'organizer/tag_list.html'

    def get(self, request, page_number):
        tags = Tag.objects.all()
        paginator = Paginator(
            tags, self.paginate_by)
        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(
                paginator.num_pages)
        if page.has_previous():
            prev_url = reverse(
                'organizer_tag_page',
                args=(
                    page.previous_page_number(),
                ))
        else:
            prev_url = None
        if page.has_next():
            next_url = reverse(
                'organizer_tag_page',
                args=(
                    page.next_page_number(),
                ))
        else:
            next_url = None
        context = {
            'is_paginated':
                page.has_other_pages(),
            'next_page_url': next_url,
            'paginator': paginator,
            'previous_page_url': prev_url,
            'tag_list': page,
        }
        return render(
            request, self.template_name, context)
"""
"""
def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    return render(request, 'organizer/tag_detail.html', {'tag': tag})
"""

class TagDetail(DetailView):
    model = Tag

#def startup_list(request):
#    return render(request, 'organizer/startup_list.html', {'startup_list': Startup.objects.all()})

class StartupList(PageLinksMixin, ListView):
    model = Startup
    paginate_by = 5
"""
    page_kwarg = 'page'
    paginate_by = 5 # 5 items per page
    template_name = 'organizer/startup_list.html'

    def get(self, request):
        startups = Startup.objects.all()
        paginator = Paginator(
            startups, self.paginate_by)
        page_number = request.GET.get(
            self.page_kwarg)
        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(
                paginator.num_pages)
        if page.has_previous():
            prev_url = "?{pkw}={n}".format(
                pkw=self.page_kwarg,
                n=page.previous_page_number())
        else:
            prev_url = None
        if page.has_next():
            next_url = "?{pkw}={n}".format(
                pkw=self.page_kwarg,
                n=page.next_page_number())
        else:
            next_url = None
        context = {
            'is_paginated':
                page.has_other_pages(),
            'next_page_url': next_url,
            'paginator': paginator,
            'previous_page_url': prev_url,
            'startup_list': page,
        }
        return render(
            request, self.template_name, context)
"""
"""
def startup_detail(request, slug):
    startup = get_object_or_404(Startup, slug__iexact=slug)
    return render(request, 'organizer/startup_detail.html', {'startup': startup})
"""

class StartupDetail(DetailView):
    model = Startup

"""
def tag_create(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            new_tag = form.save()
            return redirect(new_tag)
        #else: # empty data or invalid data
            #return render(request, 'organizer/tag_form.html', {'form': form}
    else: #request.method != 'POST'
        form = TagForm()
    return render(request, 'organizer/tag_form.html', {'form': form})
"""
class TagCreate(CreateView):
    form_class = TagForm
    model = Tag

"""
    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        else:
            return render(request, self.template_name, {'form': bound_form})
"""

class StartupCreate(CreateView):
    form_class = StartupForm
    model = Startup

"""
    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_startup = bound_form.save()
            return redirect(new_startup)
        else:
            return render(request, self.template_name, {'form': bound_form})
"""

class NewsLinkCreate(NewsLinkGetObjectMixin, StartupContextMixin, CreateView):
    form_class = NewsLinkForm
    model = NewsLink

    def get_initial(self):
        startup_slug = self.kwargs.get(self.startup_slug_url_kwarg)
        self.startup = get_object_or_404(Startup, slug__iexact=startup_slug)
        initial = {self.startup_context_object_name: self.startup, }
        initial.update(self.initial)
        return initial

"""
    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_newslink = bound_form.save()
            return redirect(new_newslink)
        else:
            return render(request, self.template_name, {'form': bound_form})
"""

class NewsLinkUpdate(NewsLinkGetObjectMixin, StartupContextMixin, UpdateView):
    form_class = NewsLinkForm
    model = NewsLink
    slug_url_kwarg = 'newslink_slug'
    #template_name_suffix = '_form_update'
"""
    template_name = ('organizer/newslink_form_update.html')

    def get(self, request, pk):
        newslink = get_object_or_404(NewsLink, pk=pk)
        context = {'form': self.form_class(instance=newslink), 'newslink': newslink, }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        newslink = get_object_or_404(NewsLink, pk=pk)
        bound_form = self.form_class(request.POST, instance=newslink)
        if bound_form.is_valid():
            new_newslink = bound_form.save()
            return redirect(new_newslink)
        else:
            context = {'form': bound_form, 'newslink': newslink, }
            return render(request, self.template_name, context)
"""
class NewsLinkDelete(StartupContextMixin, DeleteView):
    model = NewsLink
    slug_url_kwarg = 'newslink_slug'

    def get_success_url(self):
        return (self.object.startup.get_absolute_url())
"""
    def get(self, request, pk):
        newslink = get_object_or_404(NewsLink, pk=pk)
        return render(request, 'organizer/''newslink_confirm_delete.html', {'newslink': newslink})

    def post(self, request, pk):
        newslink = get_object_or_404(NewsLink, pk=pk)
        startup = newslink.startup
        newslink.delete()
        return redirect(startup)
"""

class TagUpdate(UpdateView):
    form_class = TagForm
    model = Tag
    #template_name_suffix = '_form_update'
    #template_name = ('organizer/tag_form_update.html')

class StartupUpdate(UpdateView):
    form_class = StartupForm
    model = Startup
    #template_name_suffix = '_form_update'
    #template_name = ('organizer/startup_form_update.html')

class StartupDelete(DeleteView):
    model = Startup
    success_url = reverse_lazy('organizer_startup_list')
    #template_name = ('organizer/startup_confirm_delete.html') no need for template name when using DeleteView GCBV

class TagDelete(DeleteView):
    model = Tag
    success_url = reverse_lazy('organizer_tag_list')
    #template_name = ('organizer/tag_confirm_delete.html') no need for template name when using DeleteView GCBV
