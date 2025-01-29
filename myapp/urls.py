from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('student/<int:student_id>/term/<int:term_id>/', views.student_marks, name='student_marks'),
    path('student/<int:student_id>/progress/', views.student_progress, name='student_progress'),
]