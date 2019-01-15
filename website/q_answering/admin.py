from django.contrib import admin
from .models import Question
from .models import Employee
from .models import Activity

# make sure the question data object can be viewed from the admin site
admin.site.register(Question)
admin.site.register(Employee)
admin.site.register(Activity)
