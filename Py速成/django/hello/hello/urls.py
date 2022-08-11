from django.contrib import admin
from django.urls import path, include
import debug_toolbar

from first.views import show_index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', show_index),
    path('__debug__/', include(debug_toolbar.urls)),
]

