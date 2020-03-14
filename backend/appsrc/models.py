from django.contrib.auth.models import AbstractUser
from django.db import models


DEFAULT_ROLE_ID = 1
DEFAULT_LAST_SEEN = 0
DEFAULT_STATUS_ID = 1
EMPTY_STRING = ""

class Roles(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class UserStatuses(models.Model):
    name = models.CharField(max_length=40)

class YouYodaUser(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']
    status = models.ForeignKey(UserStatuses, default=DEFAULT_STATUS_ID, on_delete=models.CASCADE)
    role = models.ForeignKey(Roles, default=DEFAULT_ROLE_ID, related_name='owner',on_delete=models.SET_DEFAULT)
    hide_my_data = models.BooleanField(default=False)
    first_name = models.CharField(max_length=20, blank=True, default='')
    last_name = models.CharField(max_length=20, blank=True, default='')
    location = models.TextField(blank=True, default='')
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    about_me = models.TextField(blank=True, default='')
    i_like = models.TextField(blank=True, default='')
    birth_date = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=13, blank=True, default='')
    avatar_url = models.CharField(max_length=255, blank=True, default='')
    is_trainer = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')
    cover_url = models.TextField(blank=True, default=EMPTY_STRING)
    last_seen = models.IntegerField(blank=False, default=DEFAULT_LAST_SEEN)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class StatusHistory(models.Model):
    usr_stat = models.ForeignKey(UserStatuses, on_delete=models.CASCADE)
    date = models.DateTimeField()
    user = models.ForeignKey(YouYodaUser, on_delete=models.CASCADE)

class UserRequests(models.Model):
    author = models.ForeignKey(YouYodaUser, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status_code = models.CharField(max_length=3)
    comment = models.TextField(blank=True, null=True)

