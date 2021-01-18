from django.contrib.auth.decorators import login_required
from django.urls import path
from dashboard import views


urlpatterns = [
    path('', login_required(views.DashboardView.as_view()), name='dashboard'),
    path('projects/<uuid:pk>/delete/', login_required(views.ProjectDeleteView.as_view()), name='dashboard'),
]