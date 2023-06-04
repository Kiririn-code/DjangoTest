from django.db import models
from django.urls import reverse


class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'postId': self.pk})

    class Meta:
        verbose_name = 'женщины'
        verbose_name_plural = 'женщиныыыы'
        ordering = ['title']


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.name
