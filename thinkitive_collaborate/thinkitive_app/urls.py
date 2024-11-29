from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('editor/<str:doc_id>/', views.editor, name='editor'),  # Document editor
    path('register/', views.register, name='register'),  # User registration
]
