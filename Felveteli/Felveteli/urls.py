from django.contrib import admin
from django.urls import path
from APP.views import index
from APP.views import feltoltes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', feltoltes),
    path('', index),
]
