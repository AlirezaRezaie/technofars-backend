from django.db import models
from django.contrib.auth.models import User
import os


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to="category_images/", blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=450, null=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    time_to_read = models.IntegerField("زمان خواندن")
    image = models.ImageField(upload_to="blog_images/", blank=True, null=True)
    categories = models.ManyToManyField(Category, related_name="blogs")
    slug = models.SlugField(unique=True, max_length=150, blank=True, allow_unicode=True)

    def save(self, *args, **kwargs):
        try:
            old_blog = Blog.objects.get(pk=self.pk)
        except:
            super().save(*args, **kwargs)
            return

        old_image = old_blog.image
        if old_image and self.pk:  # If the instance already exists in the database
            if self.image:
                if old_image != self.image:
                    if os.path.isfile(old_image.path):
                        os.remove(old_image.path)
            else:
                self.image = old_image
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.title)


class Keyword(models.Model):
    name = models.CharField("کلید واژه", max_length=100, blank=False, null=False)
    blog = models.ForeignKey(
        Blog,
        verbose_name="کلید واژه ها",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="keyword",
    )


class Comment(models.Model):
    content = models.TextField()
    name = models.TextField()

    email = models.EmailField(max_length=254)
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name="comments", default=1
    )
    ip = models.GenericIPAddressField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
