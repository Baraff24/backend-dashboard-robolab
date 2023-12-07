from django.urls import path

from .views import (UsersListAPI, UserDetailAPI,
                    CompleteProfileAPI, ItemsListAPI,
                    ItemSubmitAPI, SubmitExcel,
                    TasksListCreateAPI, TaskDetailAPI)

urlpatterns = [
    path("users/", UsersListAPI.as_view(), name="users"),
    path("users/<int:pk>/", UserDetailAPI.as_view(), name="user-detail"),
    path("users/complete-profile/", CompleteProfileAPI.as_view(),
         name="complete-profile"),
    path("items/", ItemsListAPI.as_view(), name="items-list"),
    path("items/submit/", ItemSubmitAPI.as_view(), name="submit-single-item"),
    path("items/submit-excel/", SubmitExcel.as_view(), name="submit-excel"),
    path("tasks/", TasksListCreateAPI.as_view(), name="tasks-list-create"),
    path("tasks/<int:pk>/", TaskDetailAPI.as_view(), name="task-delete"),
]
