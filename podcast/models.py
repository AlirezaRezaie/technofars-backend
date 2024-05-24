from django.db import models
from account.models import Person


class Podcast(models.Model):
    title = models.CharField("عنوان پادکست", max_length=50, null=True, blank=False)
    slug = models.SlugField(unique=True, max_length=150, blank=True, allow_unicode=True)
    created_at = models.DateTimeField(auto_now_add=True)

    description = models.CharField(
        "درباره پادکست", max_length=250, null=True, blank=False
    )
    content = models.TextField("توضیحات")

    hosts = models.ManyToManyField(Person)

    file = models.URLField(
        "لینک پادکست", max_length=128, db_index=True, unique=True, blank=True
    )
    thumbnail = models.ImageField(upload_to="podcasts/images/", blank=True, null=True)

    def __str__(self) -> str:
        return "پادکست " + self.title
