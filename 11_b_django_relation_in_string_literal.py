from django.db import models


class EmailAccount(models.Model):
    domain = models.ForeignKey('Domain')  # Domain


class Domain(models.Model):
    def get_emails(self):
        return self.emailaccount_set