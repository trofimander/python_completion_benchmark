from django.views.generic import ListView
from django.db import models

class Bar(models.Model):
    pass

class Foo(models.Model):
    bar = models.ForeignKey(Bar, on_delete="")

class PostListView(ListView):
    def get_queryset(self):
        return Foo.objects.filter(bar="")  # bar=
