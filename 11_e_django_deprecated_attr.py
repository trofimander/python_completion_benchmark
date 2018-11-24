from django.db.models import Manager

# use_for_related_fields was removed in Django 2.0

x = Manager.use_for_related_fields  # NO! use_for_related_fields
