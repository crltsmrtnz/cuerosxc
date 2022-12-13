from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core import views

urlpatterns = [
    path('', views.landing, name='landing'),
]



# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)