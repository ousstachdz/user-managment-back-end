from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class User(User):
    profile = models.OneToOneField('Profile', verbose_name=_(
        "Profile"), on_delete=models.CASCADE, primary_key=True)


class Profile(models.Model):

    MALE = 'male'
    FEMALE = 'female'

    GANDER_CHOISES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    hometown = models.CharField(_("hometown"), max_length=50)
    age = models.PositiveIntegerField(_("age"),)
    gander = models.CharField(
        _("gander"), choices=GANDER_CHOISES, max_length=6)
