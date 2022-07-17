from django.contrib import admin
from .models import all_classes


for i in all_classes:
    admin.site.register(i)
