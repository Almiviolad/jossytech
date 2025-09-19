from django.contrib import admin
from .models import Service, Message, Project
# Register your models here.
admin.site.register([Service, Message, Project])