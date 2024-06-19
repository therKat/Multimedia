from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import os


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # Thông tin thêm về phim
    duration = models.DurationField(null=True, blank=True)  # Thời lượng phim
    poster_image = models.ImageField(null=True, blank=True, upload_to='posters')  # File ảnh poster
    video_file = models.FileField(null=True, blank=True, upload_to='videos')  # File video
    director = models.CharField(max_length=100, null=True, blank=True)  # Đạo diễn
    actors = models.CharField(max_length=255, null=True, blank=True)  # Diễn viên
    reviews = models.TextField(null=True, blank=True)  # Review

    def __str__(self):
        return self.title

    def extension(self):
        if self.file:
            name, extension = os.path.splitext(self.file.name)
            return extension
        return ''

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


