from django import template
from django.db.models import Count

from ..models import Post, Category, Tag

register = template.Library()


# 这里我们首先导入 template 这个模块，然后实例化了一个 template.Library 类，
# 并将函数 show_recent_posts 装饰为 register.inclusion_tag，这样就告诉 django，这个函数是我们自定义的一个类型为 inclusion_tag 的模板标签。
# inclusion_tag 模板标签和视图函数的功能类似，它返回一个字典值，字典中的值将作为模板变量，
# 传入由 inclusion_tag 装饰器第一个参数指定的模板。当我们在模板中通过 {% show_recent_posts %}使用自己定义的模板标签时，
# django 会将指定模板的内容使用模板标签返回的模板变量渲染后替换。
# inclusion_tag 装饰器的参数 takes_context 设置为 True 时将告诉 django，
# 在渲染 _recent_posts.html 模板时，不仅传入show_recent_posts 返回的模板变量，
# 同时会传入父模板（即使用 {% show_recent_posts %} 模板标签的模板）上下文
# （可以简单理解为渲染父模板的视图函数传入父模板的模板变量以及 django 自己传入的模板变量）。
# 当然这里并没有用到这个上下文，这里只是做个简单演示，如果需要用到，就可以在模板标签函数的定义中使用 context 变量引用这个上下文。
@register.inclusion_tag('blog/inclusions/_recent_posts.html', takes_context=True)
def show_recent_posts(context, num=5):
    return {
        'recent_post_list': Post.objects.all()[:num],
    }


@register.inclusion_tag('blog/inclusions/_archives.html', takes_context=True)
def show_archives(context):
    return {
        'date_list': Post.objects.dates('created_time', 'month', order='DESC'),
    }


@register.inclusion_tag('blog/inclusions/_tags.html', takes_context=True)
def show_tags(context):
    tag_list = Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
    return {
        'tag_list': tag_list,
    }


@register.inclusion_tag('blog/inclusions/_categories.html', takes_context=True)
def show_categories(context):
    category_list = Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
    return {
        'category_list': category_list,
    }
