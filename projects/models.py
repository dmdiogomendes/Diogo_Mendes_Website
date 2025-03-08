from django.db import models
from django.utils.timezone import now

# Create your models here.

class Post(models.Model):
    CATEGORY_CHOICES = [
        ('tech', 'Tech'),
        ('design', 'Design'),
        ('thoughts', 'Thoughts'),
        ('projects ', 'Projects'),
    ]
    title = models.CharField(max_length=200)
    subTitle = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    content = models. TextField()
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='post_images/', default='post_images/image_default.jpg')

    def __str__(self):
        return f"{self.title} - {self.get_category_display()}"

