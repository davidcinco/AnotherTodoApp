from django.urls import path
from . import views

app_name = "todo"

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("update/<int:id>", views.update, name="update"),
    path("isdone/<int:id>", views.isDone, name="isdone"),
    path("delete/<int:id>", views.delete, name="delete")
]
