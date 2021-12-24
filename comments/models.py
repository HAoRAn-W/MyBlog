from django.db import models
from django.utils import timezone


class Comment(models.Model):
    name = models.CharField('name', max_length=50)
    email = models.EmailField('email')
    url = models.URLField('website', blank=True, help_text="Leave blank or start with http(s)://")
    text = models.TextField('comments')
    created_time = models.DateTimeField('created_time', default=timezone.now)
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return '{}: {}'.format(self.name, self.text[:20])
