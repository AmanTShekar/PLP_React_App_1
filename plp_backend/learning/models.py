from django.db import models
from django.utils import timezone

class Student(models.Model):
    student_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    performance_score = models.FloatField(default=0.0)
    completed_courses = models.JSONField(default=list, blank=True)  # ✅ use JSONField
    pending_courses = models.JSONField(default=list, blank=True)    # ✅ use JSONField
    remedial_needed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class SubjectScore(models.Model):
    student = models.ForeignKey(Student, related_name='subject_scores', on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    score = models.FloatField(default=0)
    remedial_needed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.name} - {self.subject}"

class LearningResource(models.Model):
    resource_id = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    difficulty_level = models.IntegerField(default=1)
    course_id = models.CharField(max_length=50)
    recommendation_priority = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Recommendation(models.Model):
    STATUS_CHOICES = (
        ("Not Started", "Not Started"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
    )
    student = models.ForeignKey(Student, related_name='recommendations', on_delete=models.CASCADE)
    resource = models.ForeignKey(LearningResource, related_name='recommendations', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Not Started")
    recommendation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.student.name} -> {self.resource.title}"
