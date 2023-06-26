from django.urls import path

from sayt.views import *

urlpatterns = [
    path("", index, name="home"),
    path("contact/", contact, name="contact"),
    path("about/", about, name="about"),
    path("couple/", couple, name="couple"),
    path("gallery/", gallery, name="gallery"),
    path("subs/", indexx, name="subs"),
]