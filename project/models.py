from django.db import models
from account.models import Person

# Create your models here.


class Project(models.Model):
    title = models.CharField("نام پروژه", max_length=100, blank=False, null=False)
    slug = models.SlugField(unique=True, max_length=150, blank=True, allow_unicode=True)
    description = models.TextField()
    creators = models.ManyToManyField(Person)
    thumbnail = models.ImageField(upload_to="project_images/", blank=True, null=True)
    website_name = models.CharField("نام وبسایت", max_length=50, blank=True, null=True)
    technologies = models.CharField(
        "تکنولوژی های استفاده شده", max_length=50, blank=True, null=True
    )
    deadline = models.CharField(
        "مدت زمان اتمام پروژه", max_length=50, blank=True, null=True
    )
    domain = models.CharField("دامنه", max_length=20, blank=True, null=True)


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="project_images/")
