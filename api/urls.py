from django.contrib.auth.decorators import login_required
from django.urls import path

from api import views


urlpatterns = [
    path('projects/', login_required(views.ProjectList.as_view()), name='projects'),
]