from django.db import models
from account.models import Person, Technology

# Create your models here.


class ProjectSubject(models.Model):
    name = models.CharField("موضوع پروژه", max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class ProjectGroup(models.Model):
    name = models.CharField("نام گروه پروژه", max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField("نام پروژه", max_length=100, blank=False, null=False)
    slug = models.SlugField(unique=True, max_length=150, blank=True, allow_unicode=True)
    content = models.TextField("جزئیات پروژه", default="")
    description = models.CharField("درباره پروژه", default="")
    creators = models.ManyToManyField(Person)
    thumbnail = models.ImageField(upload_to="project_images/", blank=True, null=True)
    website_name = models.CharField("نام وبسایت", max_length=50, blank=True, null=True)
    technologies = models.ManyToManyField(Technology)
    subject = models.ForeignKey(ProjectSubject, on_delete=models.CASCADE, default=1)
    group = models.ForeignKey(
        ProjectGroup, on_delete=models.CASCADE, null=True, blank=True
    )
    deadline = models.CharField(
        "مدت زمان اتمام پروژه", max_length=50, blank=True, null=True
    )
    domain = models.CharField("دامنه", max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    PROJECT_TYPES = [
        ("website", "وبسایت"),
        ("app", "اپلیکیشن موبایل"),
        ("ui", "طراحی ui/ux"),
        ("graphic", "گرافیک دیزاین"),
    ]

    project_type = models.CharField(
        "نوع پروژه", null=False, choices=PROJECT_TYPES, default="website"
    )

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="images"
    )
    url = models.ImageField(upload_to="project_images/")
