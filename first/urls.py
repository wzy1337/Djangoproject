from django.urls import path
from . import views #import from current directory

urlpatterns=[
    path("", views.index,name="index"),
    path("<str:name>", views.greet, name ="greet"),
    path("brian", views.brian, name="brian"),
]