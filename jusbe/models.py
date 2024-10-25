from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.mail import send_mail
from django.utils import timezone


class UserType(models.TextChoices):
    FREE = 'FREE', '無料'
    PAID = 'PAID', '有料'


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=150)
    email = models.EmailField(verbose_name='メールアドレス', unique=True)
    image = models.ImageField(null=True)
    user_type = models.CharField(max_length=10, choices=UserType.choices, default=UserType.FREE)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    create_datetime = models.DateTimeField(default=timezone.now)
    update_datetime = models.DateTimeField(auto_now=True)
    # Stripe
    stripe_customer_id = models.CharField(max_length=255, blank=True, null=True)
    stripe_card_id = models.CharField(max_length=255, blank=True, null=True)
    stripe_subscription_id = models.CharField(max_length=255, blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    @property
    def is_free(self):
        return self.user_type == UserType.FREE

    @property
    def is_paid(self):
        return self.user_type == UserType.PAID


class Category(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=150)
    create_datetime = models.DateTimeField(default=timezone.now)
    update_datetime = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Remind(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=200)
    memo = models.TextField(blank=True, null=True)
    due_datetime = models.DateTimeField(blank=True, null=True)
    is_checked = models.BooleanField(default=False)
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    category = models.ManyToManyField(Category, related_name='tags', blank=True)

    def __str__(self):
        return self.title