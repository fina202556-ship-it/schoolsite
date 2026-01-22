from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('news/', views.news, name='news'),
    path('admissions/', views.admissions, name='admissions'),
    path('academics/', views.academics, name='academics'),
    path('student-life/', views.student_life, name='student_life'),
    path('careers/', views.careers, name='careers'),
    path('contact/', views.contact, name='contact'),
    path('courses/', views.courses, name='courses'),
    path('blog/', views.blog, name='blog'),

    # Apply Now
    path('apply-now/', views.apply_now, name='apply_now'),
    path('apply-success/', views.apply_success, name='apply_success'),

    # AJAX endpoint for subjects
    path('ajax/load-subjects/', views.load_subjects, name='ajax_load_subjects'),
]
