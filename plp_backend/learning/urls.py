from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.list_students, name='list_students'),
    path('students/create/', views.create_student, name='create_student'),
    path('students/<str:student_id>/performance/', views.student_performance, name='student_performance'),
    path('resources/', views.list_resources, name='list_resources'),
    path('resources/create/', views.create_resource, name='create_resource'),
    path('resources/<str:resource_id>/', views.resource_detail, name='resource_detail'),
    path('recommendations/', views.generate_recommendations, name='generate_recommendations'),
    path('students/<str:student_id>/recommendations/', views.list_recommendations, name='list_recommendations'),
    path('recommendations/<int:rec_id>/', views.recommendation_detail_or_update, name='recommendation_detail_or_update'),
    path('students/<str:student_id>/summary/', views.student_summary, name='student_summary'),
]
