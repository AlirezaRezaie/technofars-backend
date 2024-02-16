from django.db import models


class ContactUs(models.Model):
    title = models.CharField("موضوع پیام", blank=False, null=False)
    email = models.EmailField("ایمیل فرستنده", blank=False, null=False)
    body = models.TextField("متن پیام", blank=False, null=False)
