from django.urls import path
from . import views

urlpatterns = [
    path('',views.signup),
    path('login/',views.login),
    path('token/',views.token),
    path('student-registration/',views.student_registration),
    path('student-login/',views.student_login),
    path('student-list/',views.student_listing),
    path('student-update/<int:student_id>/',views.student_update),
    path('student-delete/<int:student_id>/',views.student_delete),
]