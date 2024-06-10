from django.contrib import admin

# Register your models here.
from .models import Category, Question, Choice

admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Choice)

#registering these models through the django interface makes them accessible by 