from django.db import models
from django.utils.six import python_2_unicode_compatible


# python_2_unicode_compatible 装饰器用于兼容 Python2
@python_2_unicode_compatible
class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey('blog.Post')

    def __str__(self):
        return self.text[:20]

# 最后，这个评论是关联到某篇文章（Post）的，
# 由于一个评论只能属于一篇文章，一篇文章可以有多个评论，
# 是一对多的关系，因此这里我们使用了 ForeignKey。
