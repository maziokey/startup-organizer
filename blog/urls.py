from django.conf.urls import url

from .views import PostList, post_detail, PostCreate, PostUpdate

urlpatterns = [
    url(r'^$', PostList.as_view(), name='blog_post_list'),
    url(r'^create/$', PostCreate.as_view(), name='blog_post_create'),
    url(r'^(?P<year>\d{4})/'r'(?P<month>\d{1,2})/'r'(?P<slug>[\w\-]+)/'r'update/$', PostUpdate.as_view(), name='blog_post_update'),
    url(r'^(?P<year>\d{4})/'r'(?P<month>\d{1,2})/'r'(?P<slug>[\w\-]+)/$', post_detail, name='blog_post_detail'),
    url(r'^(?P<year>\d{4})/'r'(?P<month>\d{1,2})/'r'(?P<slug>[\w\-]+)/'r'delete/$', PostDelete.as_view(), name='blog_post_delete'),
    #url(r'^$', PostList.as_view(), {'parent_template': 'base.html'}, name='blog_post_list'),
    #url(r'^(?P<year>\d{4})/'r'(?P<month>\d{1,2})/'r'(?P<slug>[\w\-]+)/$', post_detail, {'parent_template': 'base.html'}, name='blog_post_detail'),
]
