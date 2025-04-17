from django.urls import path
from .views import ProcessAPIView, TaskStatusView


urlpatterns = [
    path("process/", ProcessAPIView.as_view(), name="process"),
    path("status/<str:task_id>/", TaskStatusView.as_view(), name="task_status")
]