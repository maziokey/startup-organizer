from io import StringIO
from django.utils.text import mark_safe

from django import template

register = template.Library()

@register.inclusion_tag('blog/includes/partial_post_list.html')
def format_post_list(context, detail_object, *args, **kwargs):
    request = context.get('request')
    opposite = kwargs.get('opposite')
    perm_button = kwargs.get('perm_button')
    future_perms = request.user.has_perm('blog.view_future_post')
    if future_perms:
        post_list = detail_object.blog_posts.all()
    else:
        post_list = detail_object.published_posts.published()
    if opposite is None:
        section_attr = ''
    elif opposite or perm_button:
        section_attr = mark_safe('class="meta one-third column"')
    else:  # opposite is an empty list
        section_attr = mark_safe(
            'class="meta offset-by-two '
            'two-thirds column"')
    return {
        'section_attr': section_attr,
        'post_list': post_list.values('title', 'slug', 'pub_date'),
    }
