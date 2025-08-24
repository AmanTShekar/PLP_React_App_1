from django.contrib import admin
from .models import Student, LearningResource, Recommendation

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "name", "performance_score")
    search_fields = ("student_id", "name")
    list_filter = ("performance_score",)

@admin.register(LearningResource)
class LearningResourceAdmin(admin.ModelAdmin):
    list_display = ("resource_id", "title", "type", "difficulty_level", "course_id")
    search_fields = ("title", "course_id")
    list_filter = ("difficulty_level", "type")

@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ("id", "student", "resource", "status")
    search_fields = ("student__name", "resource__title")
    list_filter = ("status",)
