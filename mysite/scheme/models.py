from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


CHOICES = (
    ('0', 'Choose..'),
    ('1', 'Full Name'),
    ('2', 'Job'),
    ('3', 'Company'),
    ('4', 'Integer'),
    ('5', 'Text'),
    ('6', 'Email'),
    )


class Scheme(models.Model):

    name = models.CharField(max_length=30, default="Scheme", blank=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1
    )

    name1 = models.CharField(max_length=30, default="Column", blank=True)
    name2 = models.CharField(max_length=30, default="Column", blank=True)
    name3 = models.CharField(max_length=30, default="Column", blank=True)
    name4 = models.CharField(max_length=30, default="Column", blank=True)
    name5 = models.CharField(max_length=30, default="Column", blank=True)
    name6 = models.CharField(max_length=30, default="Column", blank=True)

    type1 = models.CharField(max_length=30, choices=CHOICES, default='0')
    type2 = models.CharField(max_length=30, choices=CHOICES, default='0')
    type3 = models.CharField(max_length=30, choices=CHOICES, default='0')
    type4 = models.CharField(max_length=30, choices=CHOICES, default='0')
    type5 = models.CharField(max_length=30, choices=CHOICES, default='0')
    type6 = models.CharField(max_length=30, choices=CHOICES, default='0')

    order1 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(6)])
    order2 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(6)])
    order3 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(6)])
    order4 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(6)])
    order5 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(6)])
    order6 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(6)])

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    def __str__(self):
        return f"<{self.id} Scheme - {self.name}, by {self.user} user >"


class DataSets(models.Model):
    upload = models.FileField(blank=True)
    scheme = models.ForeignKey(Scheme, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    rows = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return f"<id {self.id} - Scheme id {self.scheme}>"