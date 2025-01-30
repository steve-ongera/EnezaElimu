from django.urls import path
from . import views

urlpatterns = [
    path('', views.general_student_list, name='student_list'),
    path('student/<int:student_id>/term/<int:term_id>/', views.student_marks, name='student_marks'),
    path('student/<int:student_id>/progress/', views.student_progress, name='student_progress'),

    path('classes/', views.class_list, name='class_list'),
    path('classes/<int:class_id>/terms/', views.term_list, name='term_list'),
    path('classes/<int:class_id>/terms/<int:term_id>/students/',  views.student_list, name='student_list'),

    # urls.py
    path('classes/<int:class_id>/terms/<int:term_id>/analysis/', views.subject_analysis, name='subject_analysis'),
    
    path('register/', views.register, name='register'),
    path('login/', views.student_login, name='login'),
    path('logout/', views.student_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    
]