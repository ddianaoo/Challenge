from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


CHOICES = (
    ('1', 'Full Name'),
    ('2', 'Job'),
    ('3', 'Company'),
    ('4', 'Integer'),
    ('5', 'Text'),
    ('6', 'Email'),
    )


class Scheme(models.Model):

    upload = models.FileField(upload_to='', blank=True)

    name = models.CharField(max_length=30, default="None", blank=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1
    )

    name1 = models.CharField(max_length=30, default="None", blank=True)
    name2 = models.CharField(max_length=30, default="None", blank=True)
    name3 = models.CharField(max_length=30, default="None", blank=True)
    name4 = models.CharField(max_length=30, default="None", blank=True)
    name5 = models.CharField(max_length=30, default="None", blank=True)
    name6 = models.CharField(max_length=30, default="None", blank=True)

    type1 = models.CharField(max_length=30, choices=CHOICES, default='1')
    type2 = models.CharField(max_length=30, choices=CHOICES, default='1')
    type3 = models.CharField(max_length=30, choices=CHOICES, default='1')
    type4 = models.CharField(max_length=30, choices=CHOICES, default='1')
    type5 = models.CharField(max_length=30, choices=CHOICES, default='1')
    type6 = models.CharField(max_length=30, choices=CHOICES, default='1')

    order1 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    order2 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    order3 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    order4 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    order5 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    order6 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    rows = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return f"<{self.id} Scheme - {self.name}, by {self.user} user >"
