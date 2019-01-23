from django.urls import path, include
from . import views

# Urlpatterns define which url will link to which view.
# e.g. views.edit view will be available at localhost/workspace/editquestion/
urlpatterns = [
    path('', views.index, name='index'),
    path('editquestion/', views.edit, name='questioneditwindow'),
    path('editquestion/update', views.updateQuestion, name='updateQuestion'),
    path('approvequestion/', views.updateApproval, name='approveQuestion'),
]
