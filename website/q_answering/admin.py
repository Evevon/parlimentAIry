from django.contrib import admin
from .models import Question, Employee, Activity, Article, Verification, OldQuestion

# make sure the question data object can be viewed from the admin site
admin.site.register(Question)
admin.site.register(Employee)
admin.site.register(Activity)
admin.site.register(Article)
admin.site.register(Verification)
admin.site.register(OldQuestion)
