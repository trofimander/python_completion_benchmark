from django.db import models

class EmailAccount(models.Model):
    domain = models.ForeignKey('Domain')

def foo():
    acc = EmailAccount()
    print(acc.domain_id)