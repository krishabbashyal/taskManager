from django.urls import path
from main import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("incompleted/", login_required(views.IncompletedView.as_view()), name = "incompleted"),
    path("completed/", login_required(views.CompletedView.as_view()), name = "completed"),
    path("taskCreate/", login_required(views.CreateTask.as_view()), name = "taskCreate"),
]
