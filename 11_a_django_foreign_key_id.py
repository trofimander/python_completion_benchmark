from django.db import models


class EmailAccount(models.Model):
    domain = models.ForeignKey('Domain')


def foo():
    acc = EmailAccount()
    print(acc.domain_id)  # domain_id


class Project(models.Model):
    def foo(self):
        pass


class ProjectPart(models.Model):
    project = models.ForeignKey(to="Project", on_delete="")

    def bar(self):
        print(self.project.foo())  # foo
