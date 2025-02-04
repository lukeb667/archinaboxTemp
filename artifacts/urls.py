from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('artifacts/', views.artifacts, name='artifacts'),
    path('stlViewer/', views.stlViewer, name='stlViewer')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)