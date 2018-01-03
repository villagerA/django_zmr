from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    # 绑定关系的写法是把网址和对应的处理函数作为参数传给 url 函数（第一个参数是网址r'^，第二个参数是处理函数views.index），
    # 另外我们还传递了另外一个参数 name，这个参数的值将作为处理函数 index 的别名，这在以后会用到。
    # url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),
    # url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',
    #     views.archives, name='archives'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',
          views.ArchivesView.as_view(), name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^about', views.about, name='about'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
    # url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
]


# 注意：在项目根目录的 blogproject\ 目录下（即 settings.py 所在的目录），原本就有一个 urls.py 文件，
# 这是整个工程项目的 URL 配置文件。而我们这里新建了一个 urls.py 文件，且位于 blog 应用下。
# 这个文件将用于 blog 应用相关的 URL 配置。不要把两个文件搞混了。
