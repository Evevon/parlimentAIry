from django.contrib import admin
from .models import Question

# make sure the question data object can be viewed from the admin site
admin.site.register(Question)
