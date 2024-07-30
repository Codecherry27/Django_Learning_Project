from django.urls import path
from . import views

urlpatterns = [
    path("blogpost/",views.blogpostlistcreate.as_view(),name="blogpost-view-create"),
    path(
        "blogpost/<int:pk>/",
         views.blogpostretriveupdatedestroy.as_view(),
         name="update",
    )
]
