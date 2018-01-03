# coding: utf-8
import markdown
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible
from django.utils.html import strip_tags

# Create your models here.
@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Post(models.Model):

    # created_time = models.DateTimeField()
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)
    # 新增 views 字段记录阅读量
    views = models.PositiveIntegerField(default=0)

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def __str__(self):
        return self.title

    # 自定义get_absolute_url方法
    # 记得从django.urls中导入reverse函数
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        # 如果没有填写摘要
        if not self.excerpt:
            # 首先实例化一个 Markdown 类，用于渲染 body 的文本
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 先将 Markdown 文本渲染成 HTML 文本
            # strip_tags 去掉 HTML 文本的全部 HTML 标签
            # 从文本摘取前 54 个字符赋给 excerpt
            self.excerpt = strip_tags(md.convert(self.body))[:54]

        # 调用父类的 save 方法将数据保存到数据库中
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_time']

# 注意到URL配置中的url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail') ，
# 我们设定的name = 'detail'在这里派上了用场。看到这个reverse函数，它的第一个参数的值是
# 'blog:detail'，意思是blog应用下的name = detail的函数，由于我们在上面通过app_name = 'blog'
# 告诉了Django这个URL模块是属于blog应用的，因此Django能够顺利地找到blog
# 应用下name为detail的视图函数，于是reverse函数会去解析这个视图函数对应的URL，我们这里
# detail对应的规则就是post / (?P < pk > [0 - 9] +) / 这个正则表达式，
# 而正则表达式部分会被后面传入的参数pk替换，所以，如果Post的id（或者pk，这里pk和id是等价的） 是
# 255的话，那么get_absolute_url函数返回的就是 / post / 255 / ，这样Post自己就生成了自己的
# URL。



# python_2_unicode_compatible 装饰器用于兼容 Python2
# created_time、modified_time。这两个列分别表示文章的创建时间和最后一次修改时间
# category和tags。这是分类与标签，分类与标签的模型我们已经定义在上面。
#
# ForeignKey
# 表明一种一对多的关联关系。比如这里我们的文章和分类的关系，一篇文章只能对应一个分类，
#
# ManyToManyField
# 表明一种多对多的关联关系，比如这里的文章和标签，一篇文章可以有多个标签，
# 而一个标签下也可以有多篇文章。反应到数据库表格中，它们的实际存储情况是这样的：