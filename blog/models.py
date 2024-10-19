from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=100, null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    rich_content = models.TextField()
    published_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
