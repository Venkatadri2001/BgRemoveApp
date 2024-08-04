from django.urls import path
from .views import image_upload_view, result_view, add_background_view

urlpatterns = [
    path('', image_upload_view, name='upload'),
    path('result/<int:pk>/', result_view, name='result'),
    path('add_background/<int:pk>/', add_background_view, name='add_background'),
]
