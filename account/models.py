from django.db import models
from django.contrib.auth.models import (
    PermissionsMixin,
    AbstractBaseUser,
    BaseUserManager,
)


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
    name = models.CharField(max_length=20, unique=True, default=DEFAULT_ROLE)

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

    about_me = models.TextField("درباره من")
    role = models.ForeignKey(Role, on_delete=models.PROTECT, default=1)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = PersonManager()

    def __str__(self):
        return str(self.first_name) + str(self.last_name)