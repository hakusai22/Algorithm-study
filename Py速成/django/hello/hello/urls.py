from django.contrib import admin
from django.urls import path, include

from first.views import show_index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', show_index),
]