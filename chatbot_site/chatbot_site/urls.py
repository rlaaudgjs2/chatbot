from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('project_site/', include('project_site.urls')),
    path('admin/', admin.site.urls),
]