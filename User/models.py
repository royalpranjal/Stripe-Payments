from django.db import models


class Person(models.Model):
    email = models.EmailField(max_length=1000, unique=True)
    customer_id = models.CharField(max_length=1000)


class Card(models.Model):
    card_id = models.CharField(max_length=1000)
    person = models.ForeignKey('Person', related_name='card')
