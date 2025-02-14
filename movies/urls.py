from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('setup.urls')), # incluirá todas as urls criadas no app setup
] 
