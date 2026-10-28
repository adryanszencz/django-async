from django.contrib import admin
from django.urls import path

from core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("sync/", views.view_sincrona, name="sync"),
    path("async/", views.view_assincrona, name="async"),
]
