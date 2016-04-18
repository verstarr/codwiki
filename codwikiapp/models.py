from __future__ import unicode_literals

from django.db import models

# ------------
# URL
# Represents a URL for URL-based content
# ------------

class URL(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(max_length=500)

# ------------
# Game
# Represents a Call of Duty video game
# ------------

class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    developers = models.ManyToManyField('Developer')
    maps = models.ManyToManyField('Map')
    guns = models.ManyToManyField('Gun')

# ------------
# Developer
# Represents a Developer of a Call of Duty game
# ------------

class Developer(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    games = models.ManyToManyField('Game')

# ------------
# Map
# Represents a Map in a Call of Duty game
# ------------

class Map(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

# ------------
# GunType
# Represents a Map in a Call of Duty game
# ------------

class GunType(models.Model):
    name = models.CharField(max_length=100)

# ------------
# Gun
# Represents a Gun in a Call of Duty game
# ------------

class Gun(models.Model):
    name = models.CharField(max_length=100)
    gun_type = models.ForeignKey(GunType)

