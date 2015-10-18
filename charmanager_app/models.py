from django.db import models
from django.contrib.auth.models import AbstractUser


class Skill(models.Model):

    title = models.CharField(max_length=255, unique=True, error_messages={
                             'unique': 'That skill already exists.'})
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title


AbstractUser._meta.get_field('email')._unique = True
AbstractUser._meta.get_field('email').blank = False


class UserCharacter(AbstractUser):

    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))
    SPECIALIZATION_CHOICES = (('Wr', 'Warrior'), ('Tm', 'Templar'),
                              ('As', 'Assassin'), ('Rg', 'Ranger'),
                              ('Sc', 'Sorcerer'), ('Sm', 'Spiritmaster'),
                              ('Hl', 'Healer'), ('Ch', 'Chanter'))

    skills = models.ManyToManyField(Skill)
    nickname = models.CharField(max_length=255, blank=True)
    level = models.PositiveIntegerField(default=1)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES)
    specialization = models.CharField(
        max_length=2, choices=SPECIALIZATION_CHOICES)
    date_edit = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
# Create your models here.
