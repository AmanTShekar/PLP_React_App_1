from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import Student, LearningResource, Recommendation
from .serializers import StudentSerializer, RecommendationSerializer, LearningResourceSerializer
from .ai import recommend_for_student
from .consumers import broadcast_recommendation_update

# ------------------------
# STUDENT ENDPOINTS
# ------------------------
@api_view(['GET'])
@permission_classes([AllowAny])
def list_students(request):
    students = Student.objects.all()
    if not students.exists():
        return Response({"detail": "No students found"}, status=status.HTTP_404_NOT_FOUND)
    
    paginator = PageNumberPagination()
    paginator.page_size = 10
    result_page = paginator.paginate_queryset(students, request)
    return paginator.get_paginated_response(StudentSerializer(result_page, many=True).data)


@api_view(['GET'])
@permission_classes([AllowAny])
def student_performance(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    data = {
        "student_id": student.student_id,
        "name": student.name,
        "performance_score": student.performance_score,
        "completed_courses": student.completed_courses,  # JSONField
        "pending_courses": student.pending_courses,      # JSONField
        "remedial_needed": student.remedial_needed,
    }
    return Response(data)


@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def create_student(request):
    required_fields = ["student_id", "name", "email"]
    for field in required_fields:
        if field not in request.data:
            return Response({"detail": f"{field} is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    ser = StudentSerializer(data=request.data)
    ser.is_valid(raise_exception=True)
    student = ser.save()
    # Auto-set remedial if performance < 60
    student.remedial_needed = student.performance_score < 60
    student.save()
    return Response(StudentSerializer(student).data, status=status.HTTP_201_CREATED)


# ------------------------
# LEARNING RESOURCE ENDPOINTS
# ------------------------
@api_view(['GET'])
@permission_classes([AllowAny])
def list_resources(request):
    resources = LearningResource.objects.all()
    if not resources.exists():
        return Response({"detail": "No resources found"}, status=status.HTTP_404_NOT_FOUND)
    
    paginator = PageNumberPagination()
    paginator.page_size = 10
    result_page = paginator.paginate_queryset(resources, request)
    return paginator.get_paginated_response(LearningResourceSerializer(result_page, many=True).data)


@api_view(['POST'])
@permission_classes([AllowAny])
def create_resource(request):
    required_fields = ["resource_id", "title", "type", "difficulty_level", "course_id"]
    for field in required_fields:
        if field not in request.data:
            return Response({"detail": f"{field} is required"}, status=status.HTTP_400_BAD_REQUEST)

    if not (1 <= int(request.data["difficulty_level"]) <= 5):
        return Response({"detail": "difficulty_level must be between 1 and 5"}, status=status.HTTP_400_BAD_REQUEST)

    ser = LearningResourceSerializer(data=request.data)
    ser.is_valid(raise_exception=True)
    resource = ser.save()
    return Response(LearningResourceSerializer(resource).data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([AllowAny])
def resource_detail(request, resource_id):
    resource = get_object_or_404(LearningResource, resource_id=resource_id)
    return Response(LearningResourceSerializer(resource).data)


# ------------------------
# RECOMMENDATION ENDPOINTS
# ------------------------
@api_view(['POST'])
@permission_classes([AllowAny])
def generate_recommendations(request):
    student_id = request.data.get('student_id')
    if not student_id:
        return Response({"detail": "student_id is required"}, status=status.HTTP_400_BAD_REQUEST)

    student = get_object_or_404(Student, student_id=student_id)
    resources = recommend_for_student(student)

    created_recs = []
    for res in resources:
        rec, created = Recommendation.objects.get_or_create(student=student, resource=res)
        if created:
            created_recs.append(rec)
            broadcast_recommendation_update(student.student_id, rec)

    return Response({
        "count": len(created_recs),
        "items": RecommendationSerializer(created_recs, many=True).data
    }, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([AllowAny])
def list_recommendations(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    recs = Recommendation.objects.filter(student=student).select_related('resource')

    # Filter recommendations:
    filtered_recs = [
        r for r in recs
        if (student.remedial_needed and r.resource.resource_id.startswith("RM"))
        or (r.resource.course_id in student.pending_courses)
    ]

    if not filtered_recs:
        return Response({"detail": "No recommendations found"}, status=status.HTTP_404_NOT_FOUND)

    paginator = PageNumberPagination()
    paginator.page_size = 10
    result_page = paginator.paginate_queryset(filtered_recs, request)
    return paginator.get_paginated_response(RecommendationSerializer(result_page, many=True).data)


@api_view(['GET', 'PATCH'])
@permission_classes([AllowAny])
def recommendation_detail_or_update(request, rec_id):
    rec = get_object_or_404(Recommendation, id=rec_id)

    if request.method == 'GET':
        return Response(RecommendationSerializer(rec).data)

    if request.method == 'PATCH':
        new_status = request.data.get("status")
        if new_status not in dict(Recommendation.STATUS_CHOICES):
            return Response({"error": "Invalid status"}, status=status.HTTP_400_BAD_REQUEST)
        rec.status = new_status
        rec.save()
        broadcast_recommendation_update(rec.student.student_id, rec)
        return Response(RecommendationSerializer(rec).data, status=status.HTTP_200_OK)


# ------------------------
# AGGREGATE / SUMMARY ENDPOINT
# ------------------------
@api_view(['GET'])
@permission_classes([AllowAny])
def student_summary(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)

    total_courses = len(student.completed_courses) + len(student.pending_courses)
    progress_pct = (len(student.completed_courses) / total_courses) * 100 if total_courses else 0

    data = {
        "student_id": student.student_id,
        "name": student.name,
        "progress_percentage": round(progress_pct, 2),
        "completed_courses": student.completed_courses,
        "pending_courses": student.pending_courses,
        "remedial_needed": student.remedial_needed
    }
    return Response(data)
