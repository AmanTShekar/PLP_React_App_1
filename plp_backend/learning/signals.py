from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student, Recommendation
from .ai import recommend_for_student
from .consumers import broadcast_recommendation_update

# ----------------------------------------
# Auto-generate recommendations for new students
# ----------------------------------------
@receiver(post_save, sender=Student)
def create_recommendations_for_new_student(sender, instance, created, **kwargs):
    if created:
        resources = recommend_for_student(instance)
        for resource in resources:
            rec, created_rec = Recommendation.objects.get_or_create(
                student=instance,
                resource=resource,
                defaults={"status": "Not Started"}
            )
            if created_rec:
                # Optional: broadcast new recommendation
                broadcast_recommendation_update(instance.student_id, rec)

# ----------------------------------------
# Broadcast updates when a recommendation is updated
# ----------------------------------------
@receiver(post_save, sender=Recommendation)
def broadcast_recommendation_status_update(sender, instance, created, **kwargs):
    if not created:
        # Only broadcast if the status changed
        broadcast_recommendation_update(instance.student.student_id, instance)
