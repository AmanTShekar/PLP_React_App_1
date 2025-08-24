from rest_framework import serializers
from .models import Student, SubjectScore, LearningResource, Recommendation

class SubjectScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectScore
        fields = ['subject', 'score', 'remedial_needed']

class LearningResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningResource
        fields = ['resource_id', 'title', 'type', 'difficulty_level', 'course_id', 'recommendation_priority']

class RecommendationSerializer(serializers.ModelSerializer):
    resource = LearningResourceSerializer(read_only=True)
    class Meta:
        model = Recommendation
        fields = ['id', 'resource', 'status', 'recommendation_date']

class StudentSerializer(serializers.ModelSerializer):
    subject_scores = SubjectScoreSerializer(many=True, read_only=True)
    class Meta:
        model = Student
        fields = ['student_id', 'name', 'email', 'performance_score', 'completed_courses', 'pending_courses', 'remedial_needed', 'subject_scores']
