from django.db import models


class Person(models.Model):
    birthday = models.DateField()


p = Person()

p.get_next_by_birthday()  # get_next_by_birthday
