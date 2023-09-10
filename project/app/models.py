from django.db import models


class Post(models.Model):
    """Модель новости."""
    post_id = models.CharField(primary_key=True, max_length=32)
    post_url = models.CharField(max_length=256)
    post_title = models.CharField(max_length=256)
    date_create = models.CharField(max_length=100)
    post_text = models.TextField()

    class Meta:
        ordering = ['-date_create']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
