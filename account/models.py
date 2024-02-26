from django.db import models
from django.contrib.auth.models import (
    PermissionsMixin,
    AbstractBaseUser,
    BaseUserManager,
)


class Technology(models.Model):
    name = models.CharField("نام تکنولوژی", blank=False, null=False)
    icon = models.ImageField(upload_to="technoloy_icon/", blank=True, null=True)

    def __str__(self):
        return self.name


class PersonManager(BaseUserManager):
    """
    cusotmized mangager for CustomUser
    """

    def create_user(self, email, password=None, **other_fields):
        """
        on create normal user
        """
        if not email:
            raise ValueError("Users must have a valid phone_number.")

        user = self.model(email=email, **other_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **other_fields):
        """
        runs on creating a super user in django
        """
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)
        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True.")

        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True.")
        if not email:
            raise ValueError("Users must have a valid email.")

        return self.create_user(email, password, **other_fields)


class Role(models.Model):
    DEFAULT_ROLE = "admin"
    name = models.CharField(max_length=100, unique=True, default=DEFAULT_ROLE)

    def __str__(self):
        return str(self.name)


class Person(AbstractBaseUser, PermissionsMixin):
    """
    custom user model
    """

    email = models.EmailField("آدرس ایمیل", max_length=255, unique=True, null=True)
    first_name = models.CharField("نام", max_length=254, blank=True)
    last_name = models.CharField("نام خانوادگی", max_length=254, blank=True)
    is_active = models.BooleanField("فعال", default=False)
    is_staff = models.BooleanField("کارمند", default=False)
    created_at = models.DateTimeField("تاریخ ایجاد", auto_now_add=True)
    update_at = models.DateTimeField("تاریخ تغییر", auto_now=True)
    profile_image = models.ImageField(
        "عکس نمایه",
        upload_to="profiles/",
        blank=True,
        null=True,
        default="profiles/dummy-profile.png",
    )

    biography = models.TextField("بیوگرافی")
    skills = models.ManyToManyField(Technology)
    about_me = models.TextField("درباره من", blank=True, null=True)
    role = models.ForeignKey(Role, on_delete=models.PROTECT, default=1)
    slug = models.SlugField(unique=True, max_length=50, null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = PersonManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Contact(models.Model):
    contact_info = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="contact",
    )
    telegram = models.CharField(max_length=50, blank=True, null=True)
    instagram = models.CharField(max_length=50, blank=True, null=True)
    linkedin = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return "Contact Info"
