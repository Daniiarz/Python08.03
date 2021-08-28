from django.urls import path

from . import views

urlpatterns = [
    path('', views.hello_view),
    path('create-post/', views.create_post),
    path('now/', views.date_view),
    path('random_number/', views.random_number),
    path('image/', views.image_view),
    path('students/', views.student_view),
]
