from django.urls import path
from . import views

urlpatterns = [
    path('api/sentence-label/', views.label_user_chat),
    path('api/image-test/', views.get_image)
]