from typing import List
from .models import Student, LearningResource

def recommend_for_student(student: Student, max_items: int = 8) -> List[LearningResource]:
    score = student.performance_score
    pending = set(student.pending_courses or [])
    base_qs = LearningResource.objects.filter(course_id__in=pending)

    if score < 60:
        qs = base_qs.filter(difficulty_level__lte=1).order_by('-recommendation_priority')
        if qs.count() < max_items:
            qs = (qs | base_qs.filter(difficulty_level=2)).distinct().order_by('-recommendation_priority')
        return list(qs[:max_items])

    if score < 80:
        easy_med = list(base_qs.filter(difficulty_level__in=[1,2]).order_by('-recommendation_priority')[:max_items//2])
        hard = list(base_qs.filter(difficulty_level=3).order_by('-recommendation_priority')[:max_items - len(easy_med)])
        return easy_med + hard

    qs = base_qs.filter(difficulty_level=3).order_by('-recommendation_priority')
    if qs.count() < max_items:
        qs = (qs | base_qs.filter(difficulty_level=2)).distinct().order_by('-recommendation_priority')
    return list(qs[:max_items])
