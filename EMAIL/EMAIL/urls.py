from django.contrib import admin
from django.urls import path
from  emailapp.views import EmailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", EmailView.as_view())
    
]
